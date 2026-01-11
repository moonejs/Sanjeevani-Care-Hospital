
from extensions import db


class Availability(db.Model):
    __tablename__='availability'
    
    id=db.Column(db.Integer,primary_key=True)
    
    day_of_week=db.Column(db.String(60),nullable=False)
    
    session=db.Column(db.String(60),nullable=False)
    
    start_time=db.Column(db.Time,nullable=False)
    
    end_time=db.Column(db.Time,nullable=False)
    
    slot_duration=db.Column(db.Integer,nullable=False)
    
    max_patients = db.Column(db.Integer, default=1)
    
    is_enabled = db.Column(db.Boolean, default=True)
    
    doctor_id=db.Column(db.Integer,db.ForeignKey("doctors.id"),nullable=False)
    
    doctor = db.relationship("Doctor", back_populates="availabilities")
    
    def __repr__(self):
        return f"<Availability {self.doctor_id} {self.day_of_week.value} {self.session.value}>"