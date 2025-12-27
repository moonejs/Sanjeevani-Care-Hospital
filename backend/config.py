from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///hms.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
