from extensions import db
from datetime import datetime

class Treatment(db.Model):
    __tablename__ = "treatments"
    
    id = db.Column(db.Integer , primary_key=True)
    
    patient_id = db.Column(db.Integer,db.ForeignKey("patients.id"),nullable=False)
    
    doctor_id = db.Column(db.Integer,db.ForeignKey("doctors.id"),nullable=False)
    
    appointment_id=db.Column(db.Integer,db.ForeignKey("appointments.id"),nullable=False,unique=True)
    
    diagnosis = db.Column(db.String(100),nullable=False)
    notes=db.Column(db.String(255))
    
    medicines =db.Column(db.JSON)
    follow_up_date=db.Column(db.Date)
    
    appointment = db.relationship("Appointment", back_populates="treatment")
    doctor = db.relationship("Doctor", back_populates="treatments")
    patient = db.relationship("Patient", back_populates="treatments")
    
    def __repr__(self):
        return f"<Treatment {self.id}>"
    
    