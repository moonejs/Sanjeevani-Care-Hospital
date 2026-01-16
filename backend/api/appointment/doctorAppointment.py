from flask_restful import Resource
from flask_security import auth_required,roles_required,roles_accepted
from flask_login import current_user
from extensions import db
from flask import request
from datetime import datetime, timedelta
from models import Doctor,Appointment,Availability


class AppointmentDetailsByDoctor(Resource):

    @auth_required("token")
    @roles_required("doctor")
    def get(self):
        
        date_str = request.args.get("date")
        if not date_str:
            return {"message": "date is required"}, 400

        appointment_date = datetime.strptime(date_str, "%Y-%m-%d").date()

        doctor_id = current_user.doctor.id
        
        appointments=Appointment.query.filter(
            Appointment.doctor_id==doctor_id,
            Appointment.appointment_date==appointment_date
        ).order_by(Appointment.start_time).all()

        result = []

        for appt in appointments:
            session = None
            availability = Availability.query.filter_by(
                doctor_id=doctor_id,
                date=appointment_date
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

        return {
            "date": date_str,
            "total": len(result),
            "appointments": result
        }, 200
        
        

