from flask_sqlalchemy import SQLAlchemy
import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY","moon-security")
    SECURITY_PASSWORD_SALT = os.environ.get(
        "SECURITY_PASSWORD_SALT",
        "moon-password-salt"
    )
    
    
    SECURITY_PASSWORD_MIN_LENGTH = 8
    SECURITY_PASSWORD_COMPLEXITY_CHECKER = True
    
    SECURITY_CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///hms.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
