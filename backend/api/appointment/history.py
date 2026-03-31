from flask_restful import Resource
from flask_security import auth_required, roles_required
from flask_login import current_user
from datetime import datetime
from flask import request
from extensions import cache
from models import  Appointment


class DoctorAppointmentsHistory(Resource):

    @auth_required("token")
    @roles_required("doctor")
    @cache.cached(
    timeout=30,
    query_string=True,
    key_prefix=lambda: f"doctor_history_{current_user.id}"
)
    def get(self):

        doctor_id = current_user.doctor.id

        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))

        query = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date <= datetime.now().date()
        )

        pagination = query.order_by(
            Appointment.appointment_date.desc(),
            Appointment.start_time.desc()
        ).paginate(page=page, per_page=per_page, error_out=False)

        appointments_data = []

        for appt in pagination.items:
            appointments_data.append({
                "id": appt.id,
                "date": appt.appointment_date.strftime("%Y-%m-%d"),
                "time": appt.start_time.strftime("%H:%M"),
                "status": appt.status,
                "type": appt.type,
                "patient": {
                    "id": appt.patient.id,
                    "name": appt.patient.name
                },
                "treatment": {
                    "diagnosis": appt.treatment.diagnosis,
                    "notes": appt.treatment.notes,
                    "medicines": appt.treatment.medicines,
                    "follow_up_date": (
                        appt.treatment.follow_up_date.strftime("%Y-%m-%d")
                        if appt.treatment and appt.treatment.follow_up_date
                        else None
                    )
                } if appt.treatment else None
            })

        return {
            "appointments": appointments_data,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": pagination.total,
                "pages": pagination.pages
            }
        }, 200
