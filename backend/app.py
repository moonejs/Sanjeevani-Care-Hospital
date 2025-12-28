from flask import Flask
from config import Config
from extensions import db , security
from flask_security import SQLAlchemyUserDatastore 
from models import User , Role
from flask_security.utils import hash_password

app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


user_datastore = SQLAlchemyUserDatastore(db,User,Role)
security.init_app(app,user_datastore)


@app.route('/')
def hello_world():
    return "<h1>Hello Mad-2</h1>"


def create_database():
    with app.app_context(): 
        db.create_all()
        
        patient_role = user_datastore.find_or_create_role(
            name="patient" , description= "Patient"
        )
        doctor_role = user_datastore.find_or_create_role(
            name="doctor" , description= "Doctor"
        )
        admin_role = user_datastore.find_or_create_role(
            name="admin" , description= "Admin"
        )
        
        if not user_datastore.find_user(email="admin@hospital.com"):
            user_datastore.create_user(
                email="admin@hospital.com",
                password=hash_password("Admin@123"),
                roles=[admin_role]
            )
        
        db.session.commit()


if __name__=='__main__':
    create_database()
    app.run(debug=True)
