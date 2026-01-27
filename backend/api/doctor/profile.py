from flask_restful import Resource
from flask_security import auth_required, roles_required
from flask_login import current_user
from flask import request
from extensions import db
import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app
from utils.files import allowed_file

def section_status(doctor):
    return {
        "personal": all([
            doctor.name,
            doctor.age,
            doctor.gender,
            doctor.contact,
            doctor.bio,
            doctor.languages_spoken,
            doctor.profile_image
        ]),

        "education": all([
            doctor.qualification,
            doctor.specialization,
            doctor.experience_years
        ]),

        "clinic": all([
            doctor.opd_timing,
            doctor.room_number,
            doctor.consultation_fee is not None  
        ]),

        "documents": bool(doctor.registration_number)
    }


def completion_percentage(sections):
    total = len(sections)
    completed = sum(1 for v in sections.values() if v)
    return int((completed / total) * 100)

class DoctorProfile(Resource):

    @auth_required("token")
    @roles_required("doctor")
    def get(self):
        doctor = current_user.doctor

        sections = section_status(doctor)

        return {
            "id": doctor.id,
            "name": doctor.name,
            "age": doctor.age,
            "gender": doctor.gender,
            "contact": doctor.contact,
            "bio": doctor.bio,
            "qualification": doctor.qualification,
            "specialization": doctor.specialization,
            "experience_years": doctor.experience_years,
            "registration_number": doctor.registration_number,
            "consultation_fee": doctor.consultation_fee,
            "opd_timing": doctor.opd_timing,
            "room_number": doctor.room_number,
            "languages_spoken": doctor.languages_spoken,
            "profile_image": (
                request.host_url + "uploads/doctors/profile/" + doctor.profile_image
                if doctor.profile_image else None
            ),

            
            "sections": sections,
            "completion_percentage": completion_percentage(sections),
            "profile_completed": all(sections.values()),

            "department_id": doctor.department_id
        }, 200
        
        
    @auth_required("token")
    @roles_required("doctor")
    def put(self):
        doctor = current_user.doctor
        data = request.form

        if "age" in data:
            doctor.age = data.get("age")

        if "gender" in data:
            doctor.gender = data.get("gender")

        if "contact" in data:
            doctor.contact = data.get("contact")

        if "bio" in data:
            doctor.bio = data.get("bio")

        if "languages_spoken" in data:
            doctor.languages_spoken = data.get("languages_spoken")

       
        if "qualification" in data:
            doctor.qualification = data.get("qualification")

        if "specialization" in data:
            doctor.specialization = data.get("specialization")

        if "experience_years" in data:
            doctor.experience_years = data.get("experience_years")

       
        if "consultation_fee" in data:
            doctor.consultation_fee = data.get("consultation_fee")

        if "opd_timing" in data:
            doctor.opd_timing = data.get("opd_timing")

        if "room_number" in data:
            doctor.room_number = data.get("room_number")

        if "emergency_available" in data:
            doctor.emergency_available = data.get("emergency_available") == "true"

        
        if "registration_number" in data:
            doctor.registration_number = data.get("registration_number")

        image = request.files.get("profile_image")
        if image and allowed_file(image.filename, current_app.config["ALLOWED_EXTENSIONS"]):

            if doctor.profile_image:
                old_path = os.path.join(
                    current_app.config["UPLOAD_FOLDER_DOCTOR"],
                    doctor.profile_image
                )
                if os.path.exists(old_path):
                    os.remove(old_path)

            ext = image.filename.rsplit(".", 1)[1].lower()
            filename = f"{uuid.uuid4()}.{ext}"
            image_path = os.path.join(
                current_app.config["UPLOAD_FOLDER_DOCTOR"],
                secure_filename(filename)
            )

            image.save(image_path)
            doctor.profile_image = filename

      
        sections = section_status(doctor)
        doctor.profile_completed = all(sections.values())

        db.session.commit()

        return {
            "message": "Doctor profile updated successfully",
            "profile_completed": doctor.profile_completed,
            "completion_percentage": completion_percentage(sections),
            "sections": sections
        }, 200

