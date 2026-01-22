from flask_restful import Resource
from flask_security import auth_required, roles_required
from flask_login import current_user
from datetime import datetime
from sqlalchemy import func
from extensions import db
from models import Patient, Appointment
from datetime import date

class PatientProfile(Resource):

    @auth_required("token")
    @roles_required("doctor")
    def get(self, patient_id):
        doctor_id = current_user.doctor.id
        patient = Patient.query.get_or_404(patient_id)

        has_access = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.patient_id == patient_id
        ).first()

        if not has_access:
            return {"message": "Unauthorized access to patient profile"}, 403
        
        patient_info = {
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender,
            "contact": patient.contact,
        }
        
        total_visits = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.patient_id == patient_id,
            Appointment.status == "completed"
        ).count()

        last_visit = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.patient_id == patient_id,
            Appointment.status == "completed"
        ).order_by(Appointment.appointment_date.desc()).first()
        
        stats = {
            "total_visits": total_visits,
            "last_visit": last_visit.appointment_date.strftime("%Y-%m-%d") if last_visit else None
        }
        
        today = datetime.now().date()
        now_time = datetime.now().time()

        current_appointment = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.patient_id == patient_id,
            Appointment.appointment_date == today,
            Appointment.status.in_(["pending", "confirmed"]),
            Appointment.start_time >= now_time
        ).order_by(Appointment.start_time).first()
        
        current_appointment_data = None
        if current_appointment:
            current_appointment_data = {
                "id": current_appointment.id,
                "date": current_appointment.appointment_date.strftime("%Y-%m-%d"),
                "time": current_appointment.start_time.strftime("%H:%M"),
                "status": current_appointment.status,
                "type": current_appointment.type
            }
        
        appointments = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.patient_id == patient_id
        ).order_by(Appointment.appointment_date.desc()).all()

        appointments_data = []

        for appt in appointments:
            treatment = appt.treatment
            appointments_data.append({
                "id": appt.id,
                "date": appt.appointment_date.strftime("%Y-%m-%d"),
                "time": appt.start_time.strftime("%H:%M"),
                "status": appt.status,
                "type": appt.type,
                "treatment": {
                    "diagnosis": treatment.diagnosis,
                    "notes": treatment.notes,
                    "medicines": treatment.medicines,
                    "follow_up_date": (treatment.follow_up_date.strftime("%Y-%m-%d")if treatment.follow_up_date else None)
                } if treatment else None
            })

        return {
            "patient": patient_info,
            "stats": stats,
            "current_appointment": current_appointment_data,
            "appointments": appointments_data,
            
        }, 200


class DoctorPatients(Resource):

    @auth_required("token")
    @roles_required("doctor")
    def get(self):
        doctor_id = current_user.doctor.id
        today = datetime.now().date()

        patients = (
            db.session.query(Patient)
            .join(Appointment, Appointment.patient_id == Patient.id)
            .filter(Appointment.doctor_id == doctor_id)
            .distinct()
            .all()
        )

        result = []

        for patient in patients:
            total_visits = Appointment.query.filter(
                Appointment.doctor_id == doctor_id,
                Appointment.patient_id == patient.id,
                Appointment.status == "completed"
            ).count()

            
            last_visit = Appointment.query.filter(
                Appointment.doctor_id == doctor_id,
                Appointment.patient_id == patient.id,
                Appointment.status == "completed"
            ).order_by(Appointment.appointment_date.desc()).first()

            
            has_active_appointment = Appointment.query.filter(
                Appointment.doctor_id == doctor_id,
                Appointment.patient_id == patient.id,
                Appointment.status.in_(["pending", "confirmed"]),
                Appointment.appointment_date >= today
            ).first() is not None

            result.append({
                "patient_id": patient.id,
                "name": patient.name,
                "age": patient.age,
                "gender": patient.gender,
                "contact": patient.contact,
                "total_visits": total_visits,
                "last_visit": (
                    last_visit.appointment_date.strftime("%Y-%m-%d")
                    if last_visit else None
                ),
                "has_active_appointment": has_active_appointment
            })

        return {
            "total_patients": len(result),
            "patients": result
        }, 200





