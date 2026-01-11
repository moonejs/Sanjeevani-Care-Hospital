
from extensions import db



class DoctorDayStatus(db.Model):
    __tablename__ = "doctor_day_status"

    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.Date, nullable=False)

    status = db.Column(db.String(60),nullable=False)

    reason = db.Column(db.String(255))
    
    doctor_id = db.Column(db.Integer,db.ForeignKey("doctors.id"),nullable=False)
    doctor = db.relationship("Doctor",back_populates="day_statuses")

    __table_args__ = (db.UniqueConstraint("doctor_id", "date", name="unique_doctor_date"),)

    def __repr__(self):
        return f"<DoctorDayStatus {self.doctor_id} {self.date} {self.status.value}>"
