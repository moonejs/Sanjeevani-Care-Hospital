from extensions import db
class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)

    services = db.Column(db.JSON, nullable=True)
    facilities = db.Column(db.JSON, nullable=True)
    
    icon = db.Column(db.String(50), nullable=False, default="building-hospital")

    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))


    building = db.Column(db.String(100))
    floor = db.Column(db.String(50))


    opd_timing = db.Column(db.String(100))
    emergency_available = db.Column(db.Boolean, default=False)

    is_active = db.Column(db.Boolean, default=True)

    doctors = db.relationship("Doctor", backref="department", lazy=True)

    def __repr__(self):
        return f"<Department {self.name}>"
