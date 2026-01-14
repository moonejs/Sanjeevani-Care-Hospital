from flask import Blueprint
from flask_restful import Api

appointment_bp=Blueprint("appointment_bp",__name__)
appointment_api=Api(appointment_bp)

from .resources import DoctorAvailability ,PatientDoctorsAvailability

appointment_api.add_resource(DoctorAvailability,"/availability")
appointment_api.add_resource(PatientDoctorsAvailability,"/appointments")