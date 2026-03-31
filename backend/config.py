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
    
    
    BASE_DIR = os.getcwd()
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads", "patients", "profile")
    UPLOAD_FOLDER_DOCTOR = os.path.join(BASE_DIR, "uploads", "doctors", "profile")


    UPLOAD_FOLDER_PATIENT = os.path.join(BASE_DIR, "uploads", "patients", "profile")
    UPLOAD_FOLDER_DOCTOR = os.path.join(BASE_DIR, "uploads", "doctors", "profile")

    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    
    MAIL_SERVER = "localhost"
    MAIL_PORT = 1025
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = "hospital@hms.com"
    
    
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_URL = "redis://localhost:6379/0"
    CACHE_DEFAULT_TIMEOUT = 60
