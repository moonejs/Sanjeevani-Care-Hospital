from flask import Blueprint
from flask_restful import Api

appointment_bp=Blueprint("appointment_bp",__name__)
appointment_api=Api(appointment_bp)

from .resources import DoctorAvailability

appointment_api.add_resource(DoctorAvailability,"/appointments")