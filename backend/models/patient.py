from extensions import db

class Patient(db.Model):
    __tablename__="patients"
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    
    contact = db.Column(db.String(15))
    address = db.Column(db.String(255))
    
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    
    profile_completed = db.Column(db.Boolean, default=False)
    appointments = db.relationship("Appointment", backref="patient", lazy=True)
    
    treatments = db.relationship("Treatment", backref="patient", lazy=True)
    
    
    
    def __repr__(self):
        return f"<patient {self.name}>"