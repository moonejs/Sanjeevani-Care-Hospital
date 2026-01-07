from flask_restful import Resource
from flask_security import auth_required
from flask import request
from flask_security.utils import hash_password
from extensions import db
from models import Patient
import extensions

class PatientRegister(Resource):
    def post(self):
        data = request.json(silent=True)
        
        field_required=["email","password"]
        
        for field in field_required:
            if field not in data:
                return {"message":f"{field} is required."},400
        
        if extensions.user_datastore.find_user(email=data["email"]):
            return {"message":"User with email id already exist"},409
        
        if len(data["password"]) <6:
            return{"message":"Password must be at least 6 characters"},400
        user = extensions.user_datastore.create_user(
            email=data["email"],
            password=hash_password(data["password"]),
            roles=["patient"]
        )
        db.session.flush()
        
        patient =Patient(
            user_id=user.id
        )
        
        db.session.add(patient)
        db.session.commit()
        
        return {"message": "Registration successful. Please complete your profile after login."}, 201