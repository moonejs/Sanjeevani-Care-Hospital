from flask import Blueprint
from flask_restful import Api

doctor_bp=Blueprint("doctor_bp",__name__)
doctor_api=Api(doctor_bp)

from .resources import DoctorDetails,DoctorResource,PatientAssignedToday,NextAppointment

from .patient_resources import PatientProfile,DoctorPatients

doctor_api.add_resource(DoctorDetails,"/doctors")
doctor_api.add_resource(DoctorResource,"/doctors/<int:id>")
doctor_api.add_resource(PatientAssignedToday,"/doctors/patients/today")
doctor_api.add_resource(NextAppointment,"/doctors/appointments/next")

doctor_api.add_resource(PatientProfile,"/doctors/patients/<int:patient_id>/profile")
doctor_api.add_resource(DoctorPatients,"/doctors/patients")

from .profile import DoctorProfile

doctor_api.add_resource(DoctorProfile,'/doctors/profile')