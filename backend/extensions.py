from flask_sqlalchemy import SQLAlchemy
from flask_security import Security ,SQLAlchemyUserDatastore
from flask_caching import Cache

cache = Cache()

db = SQLAlchemy()
security = Security()


user_datastore=None