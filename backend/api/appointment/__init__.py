from flask import Blueprint
from flask_restful import Api

appointment_bp=Blueprint("appointment_bp",__name__)
appointment_api=Api(appointment_bp)

from .availability import DoctorAvailability 
from .appointments import PatientDoctorsAvailability,PatientAppointmentBooking
from .doctorAppointment import AppointmentDetailsByDoctor,UpdateAppointmentStatus

appointment_api.add_resource(DoctorAvailability,"/availability")

appointment_api.add_resource(PatientDoctorsAvailability,"/patients/appointments")
appointment_api.add_resource(PatientAppointmentBooking,"/appointments/book")

appointment_api.add_resource(AppointmentDetailsByDoctor,"/doctors/appointments")
appointment_api.add_resource(UpdateAppointmentStatus,"/doctors/appointments/<int:appointment_id>/status")