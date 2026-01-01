from flask_restful import Resource
from flask_security import auth_required
from flask_login import current_user

class Me(Resource):
    @auth_required("token")
    def get(self):
        return {
            "email" : current_user.email,
            "roles":[role.name for role in current_user.roles],
            "id":current_user.id
        }
        
