from flask_restful import Resource
from flask_security import auth_required,roles_required,roles_accepted
from models import Doctor,Department,Appointment,Availability
from flask_security.utils import hash_password
from flask import request
import extensions
from extensions import db
from datetime import datetime, timedelta,date
from flask_login import current_user
from utils.comman import is_doctor_bookable


class DoctorDetails(Resource):
    @auth_required("token")
    @roles_accepted("admin","patient")
    def get(self):
        doctors = Doctor.query.all()
        today = date.today()
        doctors_data = []

        for d in doctors:

            confirmed_exists = Appointment.query.filter(
                Appointment.doctor_id == d.id,
                Appointment.status == "confirmed",
                Appointment.appointment_date >= today
            ).first()

            doctors_data.append({
                "id": d.id,
                "name": d.name,
                "age": d.age,
                "gender": d.gender,
                "email": d.user.email,
                "specialization": d.specialization,
                "bio": d.bio,
                "contact": d.contact,
                "qualification": d.qualification,
                "experience_years": d.experience_years,
                "room_number": d.room_number,
                "roles": d.roles,
                "registration_number": d.registration_number,
                "department": d.department.name,
                "opd_timing": d.opd_timing,
                "emergency_available": d.emergency_available,
                "consultation_fee": d.consultation_fee,
                "profile_image": (
                    request.host_url + "uploads/doctors/profile/" + d.profile_image
                    if d.profile_image else None
                ),
                "profile_completed": d.profile_completed,
                "is_bookable": is_doctor_bookable(d),
                "languages_spoken": (
                    d.languages_spoken.split(",") if d.languages_spoken else []
                ),
                "is_blocked": d.is_blocked,

                "can_block": False if confirmed_exists else True
            })

        return doctors_data, 200
    
    @auth_required("token")
    @roles_required("admin")
    def post(self):
        data=request.json
        
        required_fields = ["email", "password", "name", "specialization", "department_id"]
        
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
            user_id=user.id,
            roles=",".join(data["roles"]),
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
        
        
class NextAppointment(Resource):

    @auth_required("token")
    @roles_required("doctor")
    def get(self):

        doctor_id = current_user.doctor.id
        today = datetime.now().date()
        now_time = datetime.now().replace(second=0, microsecond=0).time()

        appointment = (
            Appointment.query
            .filter(
                Appointment.doctor_id == doctor_id,
                Appointment.appointment_date == today,
                Appointment.status == "confirmed",
                Appointment.start_time > now_time
            )
            .order_by(Appointment.start_time)
            .first()
        )

        if not appointment:
            return {"message": "No upcoming appointment"}, 200

        return {
            "appointment_id": appointment.id,
            "start_time": appointment.start_time.strftime("%H:%M"),
            "end_time": appointment.end_time.strftime("%H:%M"),
            "patient": {
                "id": appointment.patient.id,
                "name": appointment.patient.name
            },
            "type": appointment.type
        }, 200