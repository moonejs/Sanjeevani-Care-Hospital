from flask_sqlalchemy import SQLAlchemy
from flask_security import Security ,SQLAlchemyUserDatastore


db = SQLAlchemy()
security = Security()


user_datastore=None