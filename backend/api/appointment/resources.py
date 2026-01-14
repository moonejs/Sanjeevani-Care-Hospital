from flask_restful import Resource
from flask_security import auth_required,roles_required,roles_accepted
from flask_login import current_user
from extensions import db
from flask import request
from models import Availability
from datetime import datetime
from models import Doctor

def parse_time(time):
    return None if not time else datetime.strptime(time,"%H:%M").time()


class DoctorAvailability(Resource):
    
    @auth_required("token")
    @roles_accepted("doctor")
    def get(self):
        doctor_id = current_user.doctor.id
        date_str=request.args.get("date")
        
        if not date_str:
            return {"message":"Date is required "},400
        
        date=datetime.strptime(date_str,"%Y-%m-%d").date()
        
        availability=Availability.query.filter_by(
            doctor_id=doctor_id,
            date=date
        ).first()
        
        if availability:
            return{
                "date": date_str,
            "onlineBooking": availability.online_booking,
            "morning": {
                "enabled": availability.morning_enabled,
                "startTime": availability.morning_start.strftime("%H:%M") if availability.morning_start else None,
                "endTime": availability.morning_end.strftime("%H:%M") if availability.morning_end else None,
                "slotDuration": availability.morning_slot_duration,
                "maxPatients": availability.morning_max_patients
            },
            "afternoon": {
                "enabled": availability.afternoon_enabled,
                "startTime": availability.afternoon_start.strftime("%H:%M") if availability.afternoon_start else None,
                "endTime": availability.afternoon_end.strftime("%H:%M") if availability.afternoon_end else None,
                "slotDuration": availability.afternoon_slot_duration,
                "maxPatients": availability.afternoon_max_patients
            },
            "evening": {
                "enabled": availability.evening_enabled,
                "startTime": availability.evening_start.strftime("%H:%M") if availability.evening_start else None,
                "endTime": availability.evening_end.strftime("%H:%M") if availability.evening_end else None,
                "slotDuration": availability.evening_slot_duration,
                "maxPatients": availability.evening_max_patients
            }
        }, 200
        
        return {
            "date": date_str,
            "onlineBooking": False,
            "morning": {
                "enabled": False,
                "startTime": None,
                "endTime": None,
                "slotDuration": 15,
                "maxPatients": 1
            },
            "afternoon": {
                "enabled": False,
                "startTime": None,
                "endTime": None,
                "slotDuration": 15,
                "maxPatients": 1
            },
            "evening": {
                "enabled": False,
                "startTime": None,
                "endTime": None,
                "slotDuration": 15,
                "maxPatients": 1
            }
        }, 200    
            
        
    @auth_required("token")
    @roles_required("doctor")
    def post(self):
        data=request.json
        doctor_id=current_user.doctor.id
        
        if not data:
            return {"message":"Data is required"},400
        
        date=datetime.strptime(data["date"],"%Y-%m-%d").date()
        
        availability=Availability.query.filter_by(
            doctor_id=doctor_id,
            date=date
        ).first()
        
        if not availability:
            availability=Availability(
                doctor_id=doctor_id,
                date=date
            )
            db.session.add(availability)
            
        availability.online_booking=data["online_booking"]
        
        availability.morning_enabled=data["morning_enabled"]
        availability.morning_start=parse_time(data["morning"].get("from"))
        availability.morning_end=parse_time(data["morning"].get("to"))
        availability.morning_slot_duration=data["morning"].get("slot_duration",15)
        availability.morning_max_patients=data["morning"].get("max_patients",1)
        
        availability.afternoon_enabled=data["afternoon_enabled"]
        availability.afternoon_start=parse_time(data["afternoon"].get("from"))
        availability.afternoon_end=parse_time(data["afternoon"].get("to"))
        availability.afternoon_slot_duration=data["afternoon"].get("slot_duration",15)
        availability.afternoon_max_patients=data["afternoon"].get("max_patients",1)        
        
        availability.evening_enabled=data["evening_enabled"]
        availability.evening_start=parse_time(data["evening"].get("from"))
        availability.evening_end=parse_time(data["evening"].get("to"))
        availability.evening_slot_duration=data["evening"].get("slot_duration",15)
        availability.evening_max_patients=data["evening"].get("max_patients",1)
        
        
        db.session.commit()
        
        return {"message":"Availability saved successfully"},201
    
    

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

        for doctor in doctors:
            availability = Availability.query.filter_by(
                doctor_id=doctor.id,
                date=date
            ).first()

            if availability and availability.online_booking:
                doctor_data = {
                    "doctor": {
                        "id": doctor.id,
                        "name": doctor.name,
                        "department": doctor.department.name if doctor.department else None
                    },
                    "onlineBooking": True,
                    "sessions": {
                        "morning": {
                            "enabled": availability.morning_enabled,
                            "startTime": availability.morning_start.strftime("%H:%M") if availability.morning_start else None,
                            "endTime": availability.morning_end.strftime("%H:%M") if availability.morning_end else None,
                            "slotDuration": availability.morning_slot_duration,
                            "maxPatients": availability.morning_max_patients
                        },
                        "afternoon": {
                            "enabled": availability.afternoon_enabled,
                            "startTime": availability.afternoon_start.strftime("%H:%M") if availability.afternoon_start else None,
                            "endTime": availability.afternoon_end.strftime("%H:%M") if availability.afternoon_end else None,
                            "slotDuration": availability.afternoon_slot_duration,
                            "maxPatients": availability.afternoon_max_patients
                        },
                        "evening": {
                            "enabled": availability.evening_enabled,
                            "startTime": availability.evening_start.strftime("%H:%M") if availability.evening_start else None,
                            "endTime": availability.evening_end.strftime("%H:%M") if availability.evening_end else None,
                            "slotDuration": availability.evening_slot_duration,
                            "maxPatients": availability.evening_max_patients
                        }
                    }
                }
            else:
                
                doctor_data = {
                    "doctor": {
                        "id": doctor.id,
                        "name": doctor.name,
                        "department": doctor.department.name if doctor.department else None
                    },
                    "onlineBooking": False,
                    "sessions": {
                        "morning": { "enabled": False },
                        "afternoon": { "enabled": False },
                        "evening": { "enabled": False }
                    }
                }

            response.append(doctor_data)

        return {
            "date": date_str,
            "doctors": response
        }, 200

    
        
        


        