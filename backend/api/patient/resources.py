from flask_restful import Resource
from flask_security import auth_required , roles_required,roles_accepted
from extensions import db
from models import Patient,Appointment  
from flask import request
from flask_login import current_user
from datetime import datetime
class PatientList(Resource):
    @auth_required("token")
    @roles_accepted("admin")
    def get(self):
        patients=Patient.query.all()
        
        return[
            {
                "id":p.id,
                "name":p.name,
                "gender":p.gender,
                "age":p.age,
                "contact":p.contact
            }
            for p in patients
        ]
        
class PatientProfile(Resource):
    @auth_required("token")
    @roles_required("patient")
    def get(self):
        patient=current_user.patient
        
        return{
            "name":patient.name,
            "age":patient.age,
            "gender":patient.gender,
            "contact":patient.contact,
            "address":patient.address,
            "profile_completed":patient.profile_completed
        }
    
    
    
    @auth_required("token")
    @roles_required("patient")
    def put(self):
        patient=current_user.patient
        data=request.json
        
        patient.name=data["name"]
        patient.age=data["age"]
        patient.gender=data["gender"]
        patient.contact=data["contact"]
        patient.address=data["address"]
        
        patient.profile_completed=True
        
        db.session.commit()
        
        return {"message":"profile completed successfully"}
        
        
        
class PatientDashboard(Resource):

    @auth_required("token")
    @roles_required("patient")
    def get(self):

        patient_id = current_user.patient.id
        today = datetime.now().date()
        now_time = datetime.now().time()

        upcoming_appointments = Appointment.query.filter(
            Appointment.patient_id == patient_id,
            Appointment.appointment_date >= today,
            Appointment.status.in_(["pending", "confirmed"])
        ).order_by(
            Appointment.appointment_date,
            Appointment.start_time
        ).all()

        next_appointment = None
        upcoming_count = 0

        if upcoming_appointments:
            first = upcoming_appointments[0]
            upcoming_count = max(len(upcoming_appointments) - 1, 0)

            next_appointment = {
                "appointment_id": first.id,
                "doctor": {
                    "id": first.doctor.id,
                    "name": first.doctor.name,
                    "department": first.doctor.department.name
                },
                "date": first.appointment_date.strftime("%Y-%m-%d"),
                "time": first.start_time.strftime("%H:%M"),
                "status": first.status,
                "type": first.type
            }

        
        last_completed = Appointment.query.filter(
            Appointment.patient_id == patient_id,
            Appointment.status == "completed"
        ).order_by(
            Appointment.appointment_date.desc()
        ).first()

        last_visit = None

        if last_completed and last_completed.treatment:
            treatment = last_completed.treatment

            last_visit = {
                "appointment_id": last_completed.id,
                "date": last_completed.appointment_date.strftime("%Y-%m-%d"),
                "diagnosis": treatment.diagnosis,
                "medicines": treatment.medicines or [],
                "follow_up_date": (
                    treatment.follow_up_date.strftime("%Y-%m-%d")
                    if treatment.follow_up_date else None
                )
            }

        return {
            "next_appointment": next_appointment,
            "upcoming_count": upcoming_count,
            "last_visit": last_visit
        }, 200