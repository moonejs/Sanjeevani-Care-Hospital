from flask_restful import Resource
from flask import request
from flask_security import auth_required , roles_required,roles_accepted
from flask_login import current_user
from extensions import db
from models import Patient

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