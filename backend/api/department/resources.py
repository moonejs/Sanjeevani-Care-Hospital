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
                "description":d.description,
                "icon":d.icon
            }
            for d in departments
        ],200
    
    @auth_required("token")
    @roles_required("admin")
    def post(self):
        
        data=request.json
        
        field_required=["name","description","icon"]
        
        for field in field_required:
            if field not in data:
                return{"message":f"{field} is required."},400
        existing = Department.query.filter_by(name=data["name"]).first()
        if existing:
            return {"message": f"Department {data['name']} already exists"}, 409
                
        department = Department(
            name=data["name"],
            description=data["description"],
            icon=data["icon"],
            services=data.get("services", []),
            facilities=data.get("facilities", []),
            phone=data.get("phone"),
            email=data.get("email"),
            building=data.get("building"),
            floor=data.get("floor"),
            opd_timing=data.get("opd_timing"),
            emergency_available=data.get("emergency_available", False),
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
        
        return {
            "id": department.id,
            "name": department.name,
            "description": department.description,
            "icon": department.icon,
            "services": department.services,
            "facilities": department.facilities,
            "phone": department.phone,
            "email": department.email,
            "building": department.building,
            "floor": department.floor,
            "opd_timing": department.opd_timing,
            "emergency_available": department.emergency_available
        }, 200
        
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

