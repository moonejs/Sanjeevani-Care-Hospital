from flask_restful import Resource
from flask_security import auth_required,roles_required,roles_accepted
from flask_login import current_user
from extensions import db
from flask import request
from datetime import datetime, timedelta
from models import Doctor,Appointment,Availability

class PatientDoctorsAvailability(Resource):

    @auth_required("token")
    @roles_accepted("patient")
    def get(self):
        date_str = request.args.get("date")
        if not date_str:
            return {"message": "date is required"}, 400

        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        doctors = Doctor.query.all()
        response = []

        def generate_slots(start, end, duration):
            slots = []
            current = start
            while current < end:
                slots.append(current)
                current = (
                    datetime.combine(date, current)
                    + timedelta(minutes=duration)
                ).time()
            return slots

        for doctor in doctors:

            availability = Availability.query.filter_by(
                doctor_id=doctor.id,
                date=date,
                online_booking=True
            ).first()

            if not availability:
                continue

            doctor_data = {
                "doctor": {
                    "id": doctor.id,
                    "name": doctor.name,
                    "department": doctor.department.name if doctor.department else None
                },
                "sessions": {
                    "morning": [],
                    "afternoon": [],
                    "evening": []
                }
            }

            if availability.morning_enabled:
                slots = generate_slots(availability.morning_start,availability.morning_end,availability.morning_slot_duration)

                for slot in slots:
                    booked = Appointment.query.filter(
                                Appointment.doctor_id == doctor.id,
                                Appointment.appointment_date == date,
                                Appointment.start_time == slot,
                                Appointment.status.in_(["pending", "confirmed"])
                            ).count()

                    status = (
                        "available" if booked == 0 else
                        "partial" if booked < availability.morning_max_patients else
                        "full"
                    )

                    doctor_data["sessions"]["morning"].append({
                        "time": slot.strftime("%H:%M"),
                        "booked": booked,
                        "max": availability.morning_max_patients,
                        "status": status
                    })

          
            if availability.afternoon_enabled:
                slots = generate_slots(availability.afternoon_start,availability.afternoon_end,availability.afternoon_slot_duration)

                for slot in slots:
                    booked = Appointment.query.filter(
                                Appointment.doctor_id == doctor.id,
                                Appointment.appointment_date == date,
                                Appointment.start_time == slot,
                                Appointment.status.in_(["pending", "confirmed"])
                            ).count()

                    status = (
                        "available" if booked == 0 else
                        "partial" if booked < availability.afternoon_max_patients else
                        "full"
                    )

                    doctor_data["sessions"]["afternoon"].append({
                        "time": slot.strftime("%H:%M"),
                        "booked": booked,
                        "max": availability.afternoon_max_patients,
                        "status": status
                    })

        
            if availability.evening_enabled:
                slots = generate_slots(availability.evening_start,availability.evening_end,availability.evening_slot_duration)

                for slot in slots:
                    booked = Appointment.query.filter(
                                Appointment.doctor_id == doctor.id,
                                Appointment.appointment_date == date,
                                Appointment.start_time == slot,
                                Appointment.status.in_(["pending", "confirmed"])
                            ).count()

                    status = (
                        "available" if booked == 0 else
                        "partial" if booked < availability.evening_max_patients else
                        "full"
                    )

                    doctor_data["sessions"]["evening"].append({
                        "time": slot.strftime("%H:%M"),
                        "booked": booked,
                        "max": availability.evening_max_patients,
                        "status": status
                    })

            response.append(doctor_data)

        return {
            "date": date_str,
            "doctors": response
        }, 200


class PatientAppointmentBooking(Resource):

    @auth_required("token")
    @roles_required("patient")
    def post(self):
        data = request.json
        
        field_required=["doctor_id","date","start_time","type"]
        if not data:
            return {"message": "Data is required"}, 400
        
        for field in field_required:
            if field not in data:
                return {"message": f"{field} is required"}, 400
            
        if data["type"] not in ["opd", "follow_up", "emergency"]:
            return {"message": "Invalid appointment type"}, 400


        doctor_id = data.get("doctor_id")
        date_str = data.get("date")
        start_time_str = data.get("start_time")
        type=data.get("type")
        patient_id = current_user.patient.id

        appointment_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        start_time = datetime.strptime(start_time_str, "%H:%M").time()

        availability = Availability.query.filter_by(
            doctor_id=doctor_id,
            date=appointment_date,
            online_booking=True
        ).first()

        if not availability:
            return {"message": "Doctor not available on this date"}, 404

        session = None
        slot_duration = None
        max_patients = None

        def in_range(start, end, value):
            return start <= value < end


        if availability.morning_enabled and in_range(availability.morning_start, availability.morning_end, start_time):
            session = "morning"
            slot_duration = availability.morning_slot_duration
            max_patients = availability.morning_max_patients

        elif availability.afternoon_enabled and in_range(availability.afternoon_start, availability.afternoon_end, start_time):
            session = "afternoon"
            slot_duration = availability.afternoon_slot_duration
            max_patients = availability.afternoon_max_patients

        elif availability.evening_enabled and in_range(availability.evening_start, availability.evening_end, start_time):
            session = "evening"
            slot_duration = availability.evening_slot_duration
            max_patients = availability.evening_max_patients

        else:
            return {"message": "Invalid slot time"}, 400

        end_time = (datetime.combine(datetime.today(),start_time)+timedelta(minutes=int(slot_duration))).time()

        booked_count = Appointment.query.filter_by(
            doctor_id=doctor_id,
            appointment_date=appointment_date,
            start_time=start_time,
            status="confirmed"
        ).count()

        if booked_count >= max_patients:
            return {"message": "Slot already fully booked"}, 409
        
        existing = Appointment.query.filter_by(
            doctor_id=doctor_id,
            patient_id=patient_id,
            appointment_date=appointment_date,
            start_time=start_time
        ).first()

        if existing:
            return {"message": "You already booked this slot"}, 409

        
        appointment = Appointment(
            doctor_id=doctor_id,
            patient_id=patient_id,
            appointment_date=appointment_date,
            start_time=start_time,
            end_time=end_time,
            status="pending",
            type=type
        )

        db.session.add(appointment)
        db.session.commit()

        return {
            "message": "Appointment booked successfully",
            "appointment_id": appointment.id,
            "status": appointment.status
        }, 201
