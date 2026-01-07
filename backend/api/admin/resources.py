from flask_restful import Resource
from flask_security import auth_required,roles_required
from models import Doctor,Department
from flask_security.utils import hash_password
from flask import request
import extensions
from extensions import db

class DoctorDetails(Resource):
    
    @auth_required("token")
    @roles_required("admin")
    def get(self):
        doctors = Doctor.query.all()
        
        return [
            {
                "id":d.id,
                "email":d.user.email,
                "name":d.name,
                "specialization":d.specialization,
                "contact":d.contact,
                "department":d.department.name
            }
            for d in doctors
        ],200
    
    @auth_required("token")
    @roles_required("admin")
    def post(self):
        data=request.json
        
        required_fields = ["email", "password", "name", "specialization", "contact", "department_id"]
        
        for field in required_fields:
            if field not in data:
                return {
                    "message":f"{field} is required"
                },400   
        
        if extensions.user_datastore.find_user(email=data["email"]):
            return {"message":f"Doctor with {data["email"]} id already exists."},400
            
        
        user = extensions.user_datastore.create_user(
            email=data["email"],
            password=hash_password(data["password"]),
            roles=["doctor"]
        )
        
        
        department = Department.query.get(data['department_id'])
        print(department)
        if not department:
            return {"message":"Invalid Department."},400
        
        db.session.flush()
        
        doctor = Doctor(
            name=data["name"],
            specialization=data['specialization'],
            contact=data['contact'],
            user_id=user.id,
            department_id=department.id
        )
        db.session.add(doctor)
        db.session.commit()
        
        return {
            "message":"Doctor created successfully",
            "doctor_id":doctor.id
        },201
        
        
        
class DepartmentDetails(Resource):
    @auth_required("token")
    @roles_required("admin")
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
            if not field:
                return{"message":f"{field} is required."},400
        
        department=Department(
            name=data["name"],
            description=data["description"]
        )
        
        db.session.add(department)
        db.session.commit()
        
        return {"message":f"{data["name"]} Department added Successfully "}