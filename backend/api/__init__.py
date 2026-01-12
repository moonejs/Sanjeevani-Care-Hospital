from .patient import patient_bp
from .auth import auth_bp
from .admin import admin_bp
from .department import department_bp
from .doctor import doctor_bp
from .appointment import appointment_bp
all_blueprints=[patient_bp,auth_bp,admin_bp,department_bp,doctor_bp,appointment_bp]