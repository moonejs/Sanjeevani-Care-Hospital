from flask_restful import Resource
from flask_security import auth_required
from flask_login import current_user

class Me(Resource):
    @auth_required("token")
    def get(self):
        user=current_user
        if current_user.doctor and current_user.doctor.is_blocked:
            return {"message": "Account blocked"}, 403
        
        response= {
            "email" : user.email,
            "roles":[role.name for role in user.roles],
            "id":user.id
        }
        
        if user.patient:
            response["profile_completed"] = user.patient.profile_completed
            response["name"] = user.patient.name
            response["age"] = user.patient.age
            response["gender"] = user.patient.gender
            response["contact"] = user.patient.contact
            response["address"] = user.patient.address
        
        if user.doctor:
            response["name"]=user.doctor.name
            response["specialization"]=user.doctor.specialization
            response["contact"]=user.doctor.contact
            response["department"]=user.doctor.department.name
        return response