from flask import Blueprint
from flask_restful import Api

appointment_bp=Blueprint("appointment_bp",__name__)
appointment_api=Api(appointment_bp)

from .availability import DoctorAvailability 
from .appointments import PatientDoctorsAvailability,PatientAppointmentBooking

appointment_api.add_resource(DoctorAvailability,"/availability")
appointment_api.add_resource(PatientDoctorsAvailability,"/appointments")
appointment_api.add_resource(PatientAppointmentBooking,"/appointments/book")