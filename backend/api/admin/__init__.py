from flask import Blueprint
from flask_restful import Api

admin_bp=Blueprint("admin_bp",__name__)
admin_api=Api(admin_bp)

from .resources import DoctorDetails,DepartmentDetails

admin_api.add_resource(DoctorDetails,"/admin/doctors")
admin_api.add_resource(DepartmentDetails,"/admin/departments")