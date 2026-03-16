from flask import Blueprint
from flask_restful import Api

admin_bp=Blueprint("admin_bp",__name__)
admin_api=Api(admin_bp)

from .resources import AdminDashboard,BlockDoctor,UnblockDoctor

admin_api.add_resource(AdminDashboard,"/admin/dashboard")
admin_api.add_resource(BlockDoctor,'/admin/doctors/<int:doctor_id>/block')

admin_api.add_resource(UnblockDoctor, "/admin/doctors/<int:doctor_id>/unblock")
