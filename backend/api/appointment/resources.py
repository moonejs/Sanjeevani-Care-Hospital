from flask_restful import Resource
from flask_security import auth_required,roles_required,roles_accepted
from flask_login import current_user
from extensions import db
from flask import request
from models import Availability
from datetime import datetime


def parse_time(time):
    return None if not time else datetime.strptime(time,"%H:%M").time()


class DoctorAvailability(Resource):
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
        
        availability.afternoon_enabled=data["afternoon_enabled"]
        availability.afternoon_start=parse_time(data["afternoon"].get("from"))
        availability.afternoon_end=parse_time(data["afternoon"].get("to"))
        
        availability.evening_enabled=data["evening_enabled"]
        availability.evening_start=parse_time(data["evening"].get("from"))
        availability.evening_end=parse_time(data["evening"].get("to"))
        
        availability.slot_duration=data.get("slot_duration",15)
        availability.max_patients=data.get("max_patients",1)
        
        db.session.commit()
        
        return {"message","Availability saved successfully"},201
        
        