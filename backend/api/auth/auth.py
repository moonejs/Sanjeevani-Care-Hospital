from flask_restful import Resource
from flask_security import auth_required
from flask_login import current_user

class Me(Resource):
    @auth_required("token")
    def get(self):
        user=current_user
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
        
        return response