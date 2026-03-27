from flask_restful import Resource
from flask_security import auth_required, roles_required
from flask_login import current_user
from flask import request
from datetime import date, timedelta, datetime
from models import Doctor, Patient, Appointment,Department
from sqlalchemy import func
from extensions import db
class AdminDashboard(Resource):
    @auth_required("token")
    @roles_required("admin")
    def get(self):
        range_type = request.args.get("range", "today")
        today = date.today()
        if range_type == "week":
            start_date = today
            end_date = today + timedelta(days=7)
        else:
            start_date = today
            end_date = today
            
        doctors_count = Doctor.query.count()
        patients_count = Patient.query.count()
        appointments_count = Appointment.query.count()
        departments_count = Department.query.count()
        
        today_appointments = Appointment.query.filter(
            Appointment.appointment_date == today
        ).count()

        pending_appointments = Appointment.query.filter(
            Appointment.status == "pending"
        ).count()

        
        upcoming = Appointment.query.filter(
            Appointment.appointment_date >= start_date,
            Appointment.appointment_date <= end_date,
            Appointment.status.in_(["pending", "confirmed"])
        ).order_by(
            Appointment.appointment_date.asc(),
            Appointment.start_time.asc()
        ).all()
        
        
        upcoming_data = [{
            "id": appt.id,
            "patient_name": appt.patient.name,
            "doctor_name": appt.doctor.name,
            "department":appt.doctor.department.name,
            "date": appt.appointment_date.strftime("%Y-%m-%d"),
            "time": appt.start_time.strftime("%H:%M"),
            "status": appt.status,
            "session":appt.session,
            "type":appt.type
        } for appt in upcoming]
        
        status_summary = {
            "pending": 0,
            "confirmed": 0,
            "completed": 0,
            "cancelled": 0
        }
        status_counts = Appointment.query.with_entities(
            Appointment.status,
            func.count(Appointment.id)
        ).filter(
            Appointment.appointment_date >= start_date,
            Appointment.appointment_date <= end_date
        ).group_by(Appointment.status).all()
        
        for status, count in status_counts:
            status_summary[status] = count
        
        # recent = Appointment.query.order_by(Appointment.created_at.desc()).limit(5).all()
        
        # recent_activity = [{
        #     "message": f"{a.patient.name} booked appointment with {a.doctor.name}",
        #     "time": a.created_at.strftime("%Y-%m-%d %H:%M")
        # } for a in recent]
        
        return {
            "stats": {
                "doctors": doctors_count,
                "patients": patients_count,
                "appointments": appointments_count,
                "departments": departments_count,
                "today_appointments": today_appointments,
                "pending_appointments": pending_appointments
            },
            "upcoming_appointments": upcoming_data,
            "status_summary": status_summary,
            # "recent_activity": recent_activity
        }, 200
        
        
    
class BlockDoctor(Resource):

    @auth_required("token")
    @roles_required("admin")
    def post(self, doctor_id):

        doctor = Doctor.query.get_or_404(doctor_id)

        if doctor.is_blocked:
            return {"message": "Doctor already blocked"}, 400

        today = datetime.now().date()

        active_appointment = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.status == "confirmed",
            Appointment.appointment_date >= today
        ).first()

        if active_appointment:
            return {
                "message": "Doctor cannot be blocked during an ongoing appointment"
            }, 400
            
        upcoming = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.status.in_(["pending"]),
            Appointment.appointment_date >= today
        ).all()

        for appt in upcoming:
            appt.status = "cancelled"
            appt.cancel_reason = "Doctor unavailable"

        doctor.is_blocked = True
        doctor.blocked_at = datetime.now()
        
        doctor.user.active = False
        doctor.user.fs_token_uniquifier = None
        
        db.session.commit()

        return {
            "message": "Doctor blocked successfully",
            "cancelled_appointments": len(upcoming)
        }, 200
        
        
class UnblockDoctor(Resource):

    @auth_required("token")
    @roles_required("admin")
    def post(self, doctor_id):

        doctor = Doctor.query.get_or_404(doctor_id)

        if not doctor.is_blocked:
            return {"message": "Doctor is already active"}, 400

        doctor.is_blocked = False
        doctor.blocked_at = None
        doctor.block_reason = None
        
        doctor.user.active = True
        
        db.session.commit()

        return {
            "message": "Doctor unblocked successfully"
        }, 200
        
class AdminAppointments(Resource):

    @auth_required("token")
    @roles_required("admin")
    def get(self):
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))

        query = Appointment.query

        
        pagination = query.order_by(
            Appointment.appointment_date.desc(),
            Appointment.start_time.desc()
        ).paginate(page=page, per_page=per_page, error_out=False)

        appointments_data = []

        for appt in pagination.items:

            appointments_data.append({
                "id": appt.id,
                "date": appt.appointment_date.strftime("%Y-%m-%d"),
                "start_time": appt.start_time.strftime("%H:%M"),
                "end_time": appt.end_time.strftime("%H:%M"),
                "status": appt.status,
                "type": appt.type,
                "session": appt.session,

                "doctor": {
                    "id": appt.doctor.id,
                    "name": appt.doctor.name,
                    "department": appt.doctor.department.name
                },

                "patient": {
                    "id": appt.patient.id,
                    "name": appt.patient.name
                },

                "treatment": {
                    "diagnosis": appt.treatment.diagnosis,
                    "notes": appt.treatment.notes,
                    "medicines": appt.treatment.medicines,
                    "follow_up_date": (
                        appt.treatment.follow_up_date.strftime("%Y-%m-%d")
                        if appt.treatment and appt.treatment.follow_up_date
                        else None
                    )
                } if appt.treatment else None
            })

        return {
            "appointments": appointments_data,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": pagination.total,
                "pages": pagination.pages
            }
        }, 200


class AdminCancelAppointment(Resource):

    @auth_required("token")
    @roles_required("admin")
    def put(self, appointment_id):

        data = request.json
        reason = data.get("reason", "Cancelled by admin")

        appointment = Appointment.query.get(appointment_id)

        if not appointment:
            return {"message": "Appointment not found"}, 404

        
        if appointment.status == "completed":
            return {"message": "Cannot cancel completed appointment"}, 400

        today = date.today()
        max_date = today + timedelta(days=7)

        
        if not (today <= appointment.appointment_date <= max_date):
            return {"message": "Can only cancel today's or this week's appointments"}, 400

       
        appointment.status = "cancelled_by_admin"
        appointment.cancel_reason = reason

        db.session.commit()

        return {
            "message": "Appointment cancelled by admin"
        }, 200