from flask_restful import Resource
from flask_security import auth_required
from flask import request
from flask_security.utils import hash_password
from extensions import user_datastore,db
from models import Patient

class PatientRegister(Resource):
    def post(self):
        data = request.json
        
        user = user_datastore.create_user(
            email=data["email"],
            password=hash_password(data["password"]),
            roles=["patient"]
        )
        
        patient =Patient(
            user_id=user.id
        )
        
        db.session.add(patient)
        db.session.commit()
        
        return {"message": "Registration successful. Please complete your profile after login."}, 201