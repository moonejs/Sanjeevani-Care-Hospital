
from extensions import db

class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)

    doctor_id = db.Column(db.Integer,db.ForeignKey("doctors.id"),nullable=False)

    patient_id = db.Column(db.Integer,db.ForeignKey("patients.id"),nullable=False)

    appointment_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    status = db.Column(db.String(60),default="pending",nullable=False)

    type = db.Column(db.String(60),default="opd",nullable=False)

    notes = db.Column(db.Text)
    cancel_reason = db.Column(db.Text)

    
    doctor = db.relationship("Doctor", back_populates="appointments")
    patient = db.relationship("Patient",back_populates="appointments")
    treatment = db.relationship( "Treatment", back_populates="appointment", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Appointment {self.appointment_date} {self.start_time}>"
