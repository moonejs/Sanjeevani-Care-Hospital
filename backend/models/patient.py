from extensions import db

class Patient(db.Model):
    __tablename__="patients"
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    
    contact = db.Column(db.Integer)
    address = db.Column(db.String(255))
    
    height_cm = db.Column(db.Float)
    weight_kg = db.Column(db.Float)
    blood_group = db.Column(db.String(5))
    
    emergency_contact_name = db.Column(db.String(100))
    emergency_contact_number = db.Column(db.Integer)
    
    profile_image = db.Column(db.String(255))
    
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    
    profile_completed = db.Column(db.Boolean, default=False)
    appointments = db.relationship("Appointment",back_populates="patient",cascade="all, delete-orphan")
    
    treatments = db.relationship( "Treatment", back_populates="patient", cascade="all, delete-orphan"
    )
    
    
    
    def __repr__(self):
        return f"<patient {self.name}>"