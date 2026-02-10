from flask_restful import Resource
from flask_security import auth_required, roles_required
from flask_login import current_user
from flask import request
from datetime import date, timedelta, datetime
from models import Doctor, Patient, Appointment
from sqlalchemy import func
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
            "date": appt.appointment_date.strftime("%Y-%m-%d"),
            "time": appt.start_time.strftime("%H:%M"),
            "status": appt.status
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
        
        recent = Appointment.query.order_by(Appointment.created_at.desc()).limit(5).all()
        
        recent_activity = [{
            "message": f"{a.patient.name} booked appointment with {a.doctor.name}",
            "time": a.created_at.strftime("%Y-%m-%d %H:%M")
        } for a in recent]
        
        return {
            "stats": {
                "doctors": doctors_count,
                "patients": patients_count,
                "appointments": appointments_count,
                "today_appointments": today_appointments,
                "pending_appointments": pending_appointments
            },
            "upcoming_appointments": upcoming_data,
            "status_summary": status_summary,
            "recent_activity": recent_activity
        }, 200