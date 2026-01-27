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

import os


app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

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
