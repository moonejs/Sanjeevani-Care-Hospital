from flask_sqlalchemy import SQLAlchemy
from flask_security import Security ,SQLAlchemyUserDatastore
from models import User, Role

db = SQLAlchemy()
security = Security()

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
