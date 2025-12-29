from extensions import db
from datetime import datetime

class Appointment(db.Model):
    __tablename__= "appointments"
    
    id = db.Column(db.Integer , primary_key=True)
    
    patient_id = db.Column(db.Integer,db.ForeignKey("patients.id"),nullable=False)
    
    doctor_id = db.Column(db.Integer,db.ForeignKey("doctors.id"),nullable=False)
    
    appointment_time=db.Column(db.DateTime,default=datetime.utcnow)
    
    status = db.Column(db.String(20),default="scheduled")
    
    def __repr__(self):
        return f"<Appointment {self.id}>"