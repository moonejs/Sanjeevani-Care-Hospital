from extensions import db
from flask_security import UserMixin
from models import roles_users

class User(db.Model,UserMixin):
    __tablename__='users'
    
    id = db.Column(db.Integer , primary_key=True)
    email = db.Column(db.String(255) , unique=True , nullable=False)
    password = db.Column(db.String(255),nullable=False)
    active= db.Column(db.Boolean,default=True)
    
    fs_uniquifier=db.Column(db.String(64),unique=True,nullable=False)
    fs_token_uniquifier=db.Column(db.String(64),unique=True,nullable=True)
    
    roles=db.relationship("Role",secondary = roles_users , backref=db.backref("users",lazy="dynamic"))
    
    patient = db.relationship("Patient" , backref="user", uselist=False)
    
    doctor = db.relationship("Doctor",backref="user",uselist=False)
    
    def __repr__(self):
        return f"<User {self.email}>"
    
    
    