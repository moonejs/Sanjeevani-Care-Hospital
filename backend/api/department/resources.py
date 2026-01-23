from flask_restful import Resource
from flask_security import auth_required,roles_required,roles_accepted
from models import Department,Doctor

from flask import request

from extensions import db

class DepartmentDetails(Resource):
    @auth_required("token")
    @roles_accepted("admin","patient")
    def get(self):
        departments=Department.query.all()
        
        return[
            {
                "id":d.id,
                "name":d.name,
                "description":d.description
            }
            for d in departments
        ],200
    
    @auth_required("token")
    @roles_required("admin")
    def post(self):
        
        data=request.json
        
        field_required=["name","description"]
        
        for field in field_required:
            if field not in data:
                return{"message":f"{field} is required."},400
        
        department=Department(
            name=data["name"],
            description=data["description"]
        )
        
        db.session.add(department)
        db.session.commit()
        
        return {"message":f"{data["name"]} Department added Successfully "}
    

class DepartmentResource(Resource):
    @auth_required("token")
    @roles_accepted("admin","patient")
    def get(self,id):
        department=Department.query.get(id)
        
        if not department:
            return {"message":"Department no t found"},404
        
        return{
            "id":department.id,
            "name":department.name,
            "description":department.description
        },200
        
class DoctorsByDepartment(Resource):

    @auth_required("token")
    @roles_accepted("admin", "patient")
    def get(self, department_id):

        doctors = Doctor.query.filter(
            Doctor.department_id == department_id
        ).all()

        return [
            {
                "id": d.id,
                "name": d.name,
                "specialization": d.specialization,
                "contact": d.contact,
                "department": d.department.name
            }
            for d in doctors
        ], 200

