from flask import Blueprint
from flask_restful import Api

doctor_bp=Blueprint("doctor_bp",__name__)
doctor_api=Api(doctor_bp)

from .resources import DoctorDetails,DoctorResource,PatientAssignedToday

doctor_api.add_resource(DoctorDetails,"/doctors")
doctor_api.add_resource(DoctorResource,"/doctors/<int:id>")
doctor_api.add_resource(PatientAssignedToday,"/doctors/patients/today")
