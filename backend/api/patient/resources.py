from flask_restful import Resource
from flask_security import auth_required , roles_required,roles_accepted
from extensions import db,cache
from models import Patient,Appointment  
from flask import request,current_app,send_from_directory
from flask_login import current_user
from datetime import datetime
import os 
import uuid
from utils.files import allowed_file

from werkzeug.utils import secure_filename

from tasks import export_patient_treatments
from celery.result import AsyncResult
from celery_app import celery



class PatientList(Resource):
    @auth_required("token")
    @roles_accepted("admin")
    @cache.cached(timeout=60, key_prefix="patients_list")
    def get(self):
        patients=Patient.query.all()
        print("Fetching from DB...")
        return[
            {
                "id":p.id,
                "name":p.name,
                "gender":p.gender,
                "age":p.age,
                "contact":p.contact,
                "address":p.address,
                "height_cm":p.height_cm,
                "weight_kg":p.weight_kg,
                "blood_group":p.blood_group,
                "emergency_contact_name":p.emergency_contact_name,
                "emergency_contact_number":p.emergency_contact_number,
                "profile_image": (
                    request.host_url + "uploads/patients/profile/" + p.profile_image
                    if p.profile_image else None
                ),
                "profile_completed":p.profile_completed,
                "email":p.user.email, 
                
            }
            for p in patients
        ]
        
class PatientProfile(Resource):
    @auth_required("token")
    @roles_required("patient")
    def get(self):
        patient=current_user.patient
        image_url = None
        
        if patient.profile_image:
            image_url = request.host_url + f"uploads/patients/profile/{patient.profile_image}"
        
        return{
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender,
            "contact": patient.contact,
            "address": patient.address,

            "height_cm": patient.height_cm,
            "weight_kg": patient.weight_kg,
            "blood_group": patient.blood_group,

            "emergency_contact_name": patient.emergency_contact_name,
            "emergency_contact_number": patient.emergency_contact_number,

            "profile_image": image_url,
            "profile_completed": patient.profile_completed
        }
    
    
    
    @auth_required("token")
    @roles_required("patient")
    def put(self):
        patient=current_user.patient
        data=request.form
        
        patient.name = data.get("name")
        patient.age = data.get("age")
        patient.gender = data.get("gender")
        patient.contact = data.get("contact")
        patient.address = data.get("address")

        patient.height_cm = data.get("height_cm")
        patient.weight_kg = data.get("weight_kg")
        patient.blood_group = data.get("blood_group")

        patient.emergency_contact_name = data.get("emergency_contact_name")
        patient.emergency_contact_number = data.get("emergency_contact_number")
        
        image = request.files.get("profile_image")
        
        if image and allowed_file(image.filename,current_app.config["ALLOWED_EXTENSIONS"]):
            ext = image.filename.rsplit(".", 1)[1].lower()
            filename = f"{uuid.uuid4()}.{ext}"

            image_path = os.path.join(current_app.config["UPLOAD_FOLDER"],secure_filename(filename))

            image.save(image_path)
            patient.profile_image = filename
        
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
        
        
        
class ExportTreatment(Resource):
    @auth_required("token")
    @roles_required("patient")
    def post(self):
        patient=current_user.patient
        
        if not patient:
            return {"message":"Patient not found"},403
        
        task = export_patient_treatments.delay(patient.id)
        
        return {
            "message": "Export started",
            "task_id": task.id
        }, 202
        
class ExportStatus(Resource):
    @auth_required("token")
    @roles_required("patient")
    def get(self, task_id):

        task = AsyncResult(task_id, app=celery)

        if task.state == "PENDING":
            return {"status": "pending"}

        if task.state == "STARTED":
            return {"status": "processing"}

        if task.state == "SUCCESS":
            return {
                "status": "completed",
                "filename": task.result["filename"]
            }

        return {"status": "failed"}, 500