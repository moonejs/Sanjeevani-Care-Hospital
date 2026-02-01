from flask_restful import Resource
from flask_security import auth_required, roles_required
from flask_login import current_user
from models import Appointment
from flask import request

class PatientAppointmentsHistory(Resource):

    @auth_required("token")
    @roles_required("patient")
    def get(self):

        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))

        patient_id = current_user.patient.id

        query = (Appointment.query.filter(Appointment.patient_id == patient_id)
            .order_by(
                Appointment.appointment_date.desc(),
                Appointment.start_time.desc()
            )
        )
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)

        data = []

        for appt in pagination.items:
            treatment = appt.treatment

            data.append({
                "id": appt.id,
                "date": appt.appointment_date.strftime("%Y-%m-%d"),
                "time": appt.start_time.strftime("%H:%M"),
                "status": appt.status,
                "type": appt.type,

                "doctor": {
                    "id": appt.doctor.id,
                    "name": appt.doctor.name,
                    "specialization": appt.doctor.specialization
                },

                "department": {
                    "id": appt.doctor.department.id if appt.doctor.department else None,
                    "name": appt.doctor.department.name if appt.doctor.department else None
                },

                "treatment": (
                    {
                        "diagnosis": treatment.diagnosis,
                        "notes": treatment.notes,
                        "medicines": treatment.medicines,
                        "follow_up_date": (
                            treatment.follow_up_date.strftime("%Y-%m-%d")
                            if treatment.follow_up_date else None
                        )
                    }
                    if treatment else None
                )
            })

        return {
            "appointments": data,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": pagination.total,
                "pages": pagination.pages
            }
        }, 200

