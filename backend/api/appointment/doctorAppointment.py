from flask_restful import Resource
from flask_security import auth_required,roles_required,roles_accepted
from flask_login import current_user
from extensions import db,cache
from flask import request
from datetime import datetime, timedelta,date
from models import Doctor,Appointment,Availability,Treatment
from sqlalchemy import case,func


class AppointmentDetailsByDoctor(Resource):

    @auth_required("token")
    @roles_required("doctor")
    def get(self):

        date_str = request.args.get("date")
        range_type = request.args.get("range", "today")

        if not date_str:
            return {"message": "date is required"}, 400

        today = date.today()

        
        if range_type == "week":
            start_date = today
            end_date = today + timedelta(days=7)
        else:
            start_date = today
            end_date = today

        doctor_id = current_user.doctor.id

        
        appointments = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date >= start_date,
            Appointment.appointment_date <= end_date
        ).order_by(
            case(
                (Appointment.status == "pending", 1),
                (Appointment.status == "confirmed", 2),
                (Appointment.status == "completed", 3),
                (Appointment.status == "cancelled", 4),
                else_=5
            ),
            Appointment.appointment_date,
            Appointment.start_time
        ).all()

        result = []

        for appt in appointments:
            session = None

         
            availability = Availability.query.filter_by(
                doctor_id=doctor_id,
                date=appt.appointment_date
            ).first()

            if availability:
                if availability.morning_enabled and availability.morning_start <= appt.start_time < availability.morning_end:
                    session = "morning"
                elif availability.afternoon_enabled and availability.afternoon_start <= appt.start_time < availability.afternoon_end:
                    session = "afternoon"
                elif availability.evening_enabled and availability.evening_start <= appt.start_time < availability.evening_end:
                    session = "evening"

            result.append({
                "appointment_id": appt.id,
                "date": appt.appointment_date.strftime("%Y-%m-%d"),
                "time": appt.start_time.strftime("%H:%M"),
                "end_time": appt.end_time.strftime("%H:%M") if appt.end_time else None,
                "patient": {
                    "id": appt.patient.id,
                    "name": appt.patient.name
                },
                "type": appt.type,
                "status": appt.status,
                "session": session
            })

        
        stats = (
            db.session.query(
                Appointment.status,
                func.count(Appointment.id)
            )
            .filter(
                Appointment.doctor_id == doctor_id,
                Appointment.appointment_date >= start_date,
                Appointment.appointment_date <= end_date
            )
            .group_by(Appointment.status)
            .all()
        )

        summary = {
            "Total": 0,
            "completed": 0,
            "confirmed": 0,
            "pending": 0,
            "cancelled": 0
        }

        for status, count in stats:
            summary[status] = count

        summary["Total"] = sum(summary.values())

        return {
            "range": range_type,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "total": len(result),
            "appointments": result,
            "summary": summary
        }, 200 

class UpdateAppointmentStatus(Resource):

    @auth_required("token")
    @roles_required("doctor")
    def patch(self, appointment_id):
        data = request.json
        if not data or "status" not in data:
            return {"message": "status is required"}, 400

        new_status = data["status"]
        allowed_status = ["confirmed", "cancelled",]

        if new_status not in allowed_status:
            return {"message": "Invalid status"}, 400

        appointment = Appointment.query.get(appointment_id)

        if not appointment:
            return {"message": "Appointment not found"}, 404

        
        if appointment.doctor_id != current_user.doctor.id:
            return {"message": "Unauthorized"}, 403

        
        if appointment.status == "cancelled":
            return {"message": "Cancelled appointments cannot be updated"}, 409

        appointment.status = new_status
        db.session.commit()
        cache.delete("admin_dashboard")
        cache.delete("doctors_list") 
        return {
            "message": f"Appointment {new_status}",
            "appointment_id": appointment.id,
            "status": appointment.status
        }, 200
      
class CompleteAppointment(Resource):

    @auth_required("token")
    @roles_required("doctor")
    def post(self, appointment_id):

        appointment = Appointment.query.get_or_404(appointment_id)

        if appointment.doctor_id != current_user.doctor.id:
            return {"message": "Unauthorized"}, 403

        if appointment.status != "confirmed":
            return {"message": "Only confirmed appointments can be completed"}, 409

        if appointment.treatment:
            return {"message": "Visit already completed"}, 409

        data = request.json
        if not data:
            return {"message": "Visit data required"}, 400
        
        
        if "diagnosis" not in data or not data["diagnosis"].strip():
            return {"message": "diagnosis is required"}, 400
        
        follow_up_date = None
        if data.get("follow_up_date"):
            try:
                follow_up_date = datetime.strptime(
                    data["follow_up_date"], "%Y-%m-%d"
                ).date()
            except ValueError:
                return {"message": "Invalid follow_up_date format (YYYY-MM-DD)"}, 400
            
        treatment = Treatment(
            appointment_id=appointment.id,
            doctor_id=appointment.doctor_id,
            patient_id=appointment.patient_id,
            diagnosis=data.get("diagnosis"),
            notes=data.get("notes"),
            medicines=data.get("medicines",[]),
            follow_up_date = follow_up_date
        )

        appointment.status = "completed"

        db.session.add(treatment)
        db.session.commit()
        cache.delete("admin_dashboard")
        cache.delete("doctors_list")
        return {
            "message": "Visit completed successfully",
            "appointment_id": appointment.id
        }, 201

