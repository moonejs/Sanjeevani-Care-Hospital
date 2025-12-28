from extensions import db
from datetime import datetime

class Treatment(db.Model):
    __tablename__ = "treatments"
    
    id = db.Column(db.Integer , primary_key=True)
    
    patient_id = db.Column(db.Integer,db.ForeignKey("patients.id"),nullable=False)
    
    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        nullable=False
    )
    
    description = db.Column(db.String(255),nullable=False)
    treatment_date = db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Treatment {self.id}>"
    
    