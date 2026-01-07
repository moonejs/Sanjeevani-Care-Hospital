from flask_restful import Resource
from flask_security import auth_required , roles_required,roles_accepted
from extensions import db
from models import Patient  
from flask import request
from flask_login import current_user
class PatientList(Resource):
    @auth_required("token")
    @roles_accepted("admin","doctor")
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
        
        