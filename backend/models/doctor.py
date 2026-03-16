from extensions import db

class Doctor(db.Model):
    __tablename__="doctors"
    
    id=db.Column(db.Integer,primary_key=True)
    
    name = db.Column(db.String(100),nullable=False)
    specialization = db.Column(db.String(100),nullable=False)
    contact = db.Column(db.String(15))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    
    roles = db.Column(db.String(100)) 
    
    is_blocked = db.Column(db.Boolean, default=False)

    blocked_at = db.Column(db.DateTime)
    block_reason = db.Column(db.Text)
    
    
    
    qualification = db.Column(db.String(100))
    experience_years = db.Column(db.Integer)
    registration_number = db.Column(db.String(50))
    bio = db.Column(db.Text)
    consultation_fee = db.Column(db.Integer)
    
    opd_timing = db.Column(db.String(100))
    emergency_available = db.Column(db.Boolean, default=False)
    room_number = db.Column(db.String(20))
    
    profile_image = db.Column(db.String(255))
    languages_spoken = db.Column(db.String(255)) 
    
    profile_completed = db.Column(db.Boolean, default=False)
    
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    
    appointments = db.relationship("Appointment",back_populates="doctor",cascade="all, delete-orphan")

    availabilities = db.relationship("Availability",back_populates="doctor",cascade="all, delete-orphan")


    department_id = db.Column(db.Integer,db.ForeignKey("departments.id"),nullable=False)
    
    treatments = db.relationship( "Treatment", back_populates="doctor", cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<doctor {self.name}>"