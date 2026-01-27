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

class DoctorProfile(Resource):

    @auth_required("token")
    @roles_required("doctor")
    def get(self):
        doctor = current_user.doctor

        return {
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization,
            "age":doctor.age,
            "gender":doctor.gender,
            "contact": doctor.contact,
            "qualification": doctor.qualification,
            "experience_years": doctor.experience_years,
            "registration_number": doctor.registration_number,
            "bio": doctor.bio,
            "roles":doctor.roles,
            "consultation_fee": doctor.consultation_fee,
            "opd_timing": doctor.opd_timing,
            "emergency_available": doctor.emergency_available,
            "room_number": doctor.room_number,
            "languages_spoken": doctor.languages_spoken,
            "profile_image": (
                request.host_url + "uploads/doctors/profile/" + doctor.profile_image
                if doctor.profile_image else None
            ),
            "profile_completed": doctor.profile_completed,
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

        if "qualification" in data:
            doctor.qualification = data.get("qualification")

        if "experience_years" in data:
            doctor.experience_years = data.get("experience_years")

        if "registration_number" in data:
            doctor.registration_number = data.get("registration_number")

        if "bio" in data:
            doctor.bio = data.get("bio")

        if "consultation_fee" in data:
            doctor.consultation_fee = data.get("consultation_fee")

        if "opd_timing" in data:
            doctor.opd_timing = data.get("opd_timing")

        if "emergency_available" in data:
            doctor.emergency_available = data.get("emergency_available") == "true"

        if "room_number" in data:
            doctor.room_number = data.get("room_number")

        if "languages_spoken" in data:
            doctor.languages_spoken = data.get("languages_spoken")

        if "roles" in data:
            doctor.roles = ",".join(data.getlist("roles"))

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

        doctor.profile_completed = True
        db.session.commit()

        return {
            "message": "Doctor profile updated successfully",
            "profile_completed": doctor.profile_completed
        }, 200
