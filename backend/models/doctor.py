from extensions import db

class Doctor(db.Model):
    __tablename__="doctors"
    
    id=db.Column(db.Integer,primary_key=True)
    
    name = db.Column(db.String(100),nullable=False)
    
    specialization = db.Column(db.String(100),nullable=False)
    
    contact = db.Column(db.String(15))
    
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    
    appointments = db.relationship("Appointment",back_populates="doctor",cascade="all, delete-orphan")

    availabilities = db.relationship("Availability",back_populates="doctor",cascade="all, delete-orphan")

    day_statuses = db.relationship("DoctorDayStatus",back_populates="doctor",cascade="all, delete-orphan")

    department_id = db.Column(db.Integer,db.ForeignKey("departments.id"),nullable=False)
    
    
    def __repr__(self):
        return f"<doctor {self.name}>"