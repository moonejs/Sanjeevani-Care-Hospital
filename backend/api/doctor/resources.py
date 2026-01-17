from flask_restful import Resource
from flask_security import auth_required,roles_required,roles_accepted
from models import Doctor,Department,Appointment
from flask_security.utils import hash_password
from flask import request
import extensions
from extensions import db
from datetime import datetime, timedelta
from flask_login import current_user

class DoctorDetails(Resource):
    
    @auth_required("token")
    @roles_accepted("admin","patient")
    def get(self):
        doctors = Doctor.query.all()
        
        return [
            {
                "id":d.id,
                "email":d.user.email,
                "name":d.name,
                "specialization":d.specialization,
                "contact":d.contact,
                "department":d.department.name
            }
            for d in doctors
        ],200
    
    @auth_required("token")
    @roles_required("admin")
    def post(self):
        data=request.json
        
        required_fields = ["email", "password", "name", "specialization", "contact", "department_id"]
        
        for field in required_fields:
            if field not in data:
                return {
                    "message":f"{field} is required"
                },400   
        
        if extensions.user_datastore.find_user(email=data["email"]):
            return {"message":f"Doctor with {data["email"]} id already exists."},400
            
        
        user = extensions.user_datastore.create_user(
            email=data["email"],
            password=hash_password(data["password"]),
            roles=["doctor"]
        )
        
        
        department = Department.query.get(data['department_id'])
        print(department)
        if not department:
            return {"message":"Invalid Department."},400
        
        db.session.flush()
        
        doctor = Doctor(
            name=data["name"],
            specialization=data['specialization'],
            contact=data['contact'],
            user_id=user.id,
            department_id=department.id
        )
        db.session.add(doctor)
        db.session.commit()
        
        return {
            "message":"Doctor created successfully",
            "doctor_id":doctor.id
        },201
        

class DoctorResource(Resource):
    @auth_required("token")
    @roles_accepted("admin","patient")
    def get(self,id):
        doctor=Doctor.query.get(id)
        
        if not doctor:
            return{"message","Doctor Not found"},404
        
        return{
            "id":doctor.id,
            "name":doctor.name,
            "specialization":doctor.specialization,
            "contact":doctor.contact,
        },200
        
        
class PatientAssignedToday(Resource):
    @auth_required("token")
    @roles_required("doctor")
    def get(self):
        date_str=request.args.get("date")
        if not date_str:
            return {"message":"Date is required"},400
        
        appointment_date=datetime.strptime(date_str,"%Y-%m-%d").date()
        
        doctor_id=current_user.doctor.id
        
        appointments= Appointment.query.filter(
            Appointment.doctor_id==doctor_id,
            Appointment.appointment_date==appointment_date,
            Appointment.status.in_(["pending","confirmed"])
            
        ).all()
        
        patients=[]
        seen_patient_ids=set()
        
        if appointments:
            for appt in appointments:
                if appt.patient_id in seen_patient_ids:
                    continue
                
                seen_patient_ids.add(appt.patient_id)
                
                total_visits = Appointment.query.filter(
                    Appointment.doctor_id == doctor_id,
                    Appointment.patient_id == appt.patient_id,
                    Appointment.status == "completed"
                ).count()
                
                last_visit = Appointment.query.filter(
                    Appointment.doctor_id == doctor_id,
                    Appointment.patient_id == appt.patient_id,
                    Appointment.status == "completed",
                    Appointment.appointment_date < appointment_date
                ).order_by(Appointment.appointment_date.desc()).first()
                
                patients.append({
                    "patient_id": appt.patient.id,
                    "name": appt.patient.name,
                    "appointment_id": appt.id,
                    "time": appt.start_time.strftime("%H:%M"),
                    "status": appt.status,
                    "type": appt.type,
                    "age":appt.patient.age,
                    "gender":appt.patient.gender,
                    "last_visit":last_visit.appointment_date.strftime("%Y-%m-%d") if last_visit else None,
                    "visits":total_visits
                })
                
        
        return {
            "date":date_str,
            "total_patients":len(patients),
            "patients":patients
        },200
        