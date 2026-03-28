from flask import Flask,send_from_directory,current_app
from config import Config
from extensions import db , security 

from flask_security.utils import hash_password
from flask_restful import Api
from api import all_blueprints
from models import User, Role
from flask_cors import CORS
from flask_security import SQLAlchemyUserDatastore
import extensions
from celery_app import celery, init_celery
import os
from tasks import generate_appointment_pdf,export_all_doctors_csv, generate_doctor_profile_pdf,export_all_appointments_csv
from celery.result import AsyncResult

app=Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

init_celery(app)

CORS(app,origins=["http://127.0.0.1:5000","http://localhost:5173"],supports_credentials=True,
    allow_headers=[
        "Content-Type",
        "Authorization",
        "Authentication-Token"
    ])

extensions.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security.init_app(app,extensions.user_datastore)

user_datastore=extensions.user_datastore

api=Api(app)

for bp in all_blueprints:
    app.register_blueprint(bp,url_prefix="/api")


@app.route('/')
def hello_world():
    return "<h1>Hello Mad-2</h1>"

@app.route("/uploads/doctors/profile/<filename>")
def doctor_profile_image(filename):
    return send_from_directory(
        current_app.config["UPLOAD_FOLDER_DOCTOR"],
        filename
    )

@app.route("/uploads/patients/profile/<filename>")
def patient_profile_image(filename):
    return send_from_directory(
        current_app.config["UPLOAD_FOLDER_PATIENT"],
        filename
    )

@app.route("/exports/<filename>")
def download_file(filename):
    return send_from_directory("exports", filename, as_attachment=True)

@app.route("/export-appointment/<int:id>")
def export_appointment(id):
    task = generate_appointment_pdf.delay(id)
    return {"task_id": task.id}

@app.route("/export-status/<task_id>")
def export_status(task_id):
    task = celery.AsyncResult(task_id)   

    print("STATE:", task.state)
    print("RESULT:", task.result)

    if task.state == "PENDING":
        return {"status": "pending"}

    elif task.state == "SUCCESS":
        return {
            "status": "completed",
            "filename": task.result.get("filename")
        }

    elif task.state == "FAILURE":
        return {"status": "failed"}

    return {"status": task.state}

@app.route("/export-doctors")
def export_doctors():
    task = export_all_doctors_csv.delay()
    return {"task_id": task.id}


@app.route("/export-doctor/<int:id>")
def export_doctor_profile(id):
    task = generate_doctor_profile_pdf.delay(id)
    return {"task_id": task.id}

@app.route("/export-appointments")
def export_appointments():
    task = export_all_appointments_csv.delay()
    return {"task_id": task.id}


def create_database():
    with app.app_context():
            
        db.create_all()
        patient_role = user_datastore.find_or_create_role(
            name="patient" , description= "Patient"
        )
        doctor_role = user_datastore.find_or_create_role(
            name="doctor" , description= "Doctor"
        )
        admin_role = user_datastore.find_or_create_role(
            name="admin" , description= "Admin"
        )
        
        if not user_datastore.find_user(email="admin@hospital.com"):
            user_datastore.create_user(
                email="admin@hospital.com",
                password=hash_password("Admin@123"),
                roles=[admin_role]
            )
        
        db.session.commit()


if __name__=='__main__':
    create_database()
    app.run(debug=True)

from tasks import *