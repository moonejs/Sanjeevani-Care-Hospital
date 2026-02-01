from flask import Blueprint
from flask_restful import Api

appointment_bp=Blueprint("appointment_bp",__name__)
appointment_api=Api(appointment_bp)

from .availability import DoctorAvailability 
from .appointments import PatientDoctorsAvailability,PatientAppointmentBooking,PatientRescheduleAppointment
from .doctorAppointment import AppointmentDetailsByDoctor,UpdateAppointmentStatus,CompleteAppointment
from .history import DoctorAppointmentsHistory
from .patientAppointments import PatientAppointmentsHistory

appointment_api.add_resource(DoctorAvailability,"/availability")

appointment_api.add_resource(PatientDoctorsAvailability,"/patients/appointments")
appointment_api.add_resource(PatientAppointmentBooking,"/appointments/book")
appointment_api.add_resource(PatientRescheduleAppointment,"/appointments/reschedule/<int:appointment_id>")


appointment_api.add_resource(AppointmentDetailsByDoctor,"/doctors/appointments")
appointment_api.add_resource(UpdateAppointmentStatus,"/doctors/appointments/<int:appointment_id>/status")
appointment_api.add_resource(CompleteAppointment,"/doctors/appointments/<int:appointment_id>/complete")


appointment_api.add_resource(DoctorAppointmentsHistory,"/doctors/appointments/history")


appointment_api.add_resource(PatientAppointmentsHistory,"/patients/appointments/history")
