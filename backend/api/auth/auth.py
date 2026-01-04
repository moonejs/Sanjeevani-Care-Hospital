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
        
        return response