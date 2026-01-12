
from extensions import db


class Availability(db.Model):
    __tablename__='availability'
    
    id = db.Column(db.Integer, primary_key=True)

    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)

    online_booking = db.Column(db.Boolean, default=False)

    morning_enabled = db.Column(db.Boolean, default=False)
    morning_start = db.Column(db.Time)
    morning_end = db.Column(db.Time)

    afternoon_enabled = db.Column(db.Boolean, default=False)
    afternoon_start = db.Column(db.Time)
    afternoon_end = db.Column(db.Time)


    evening_enabled = db.Column(db.Boolean, default=False)
    evening_start = db.Column(db.Time)
    evening_end = db.Column(db.Time)

    slot_duration = db.Column(db.Integer, default=15)
    max_patients = db.Column(db.Integer, default=1)

    doctor = db.relationship("Doctor", back_populates="availabilities")

    __table_args__ = (
        db.UniqueConstraint("doctor_id", "date", name="unique_doctor_date"),
    )
    
    def __repr__(self):
        return f"<Availability {self.doctor_id} {self.day_of_week.value} {self.session.value}>"