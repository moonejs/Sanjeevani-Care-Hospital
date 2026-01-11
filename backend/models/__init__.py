from extensions import db

roles_users = db.Table(
    "roles_users",
    db.Column("user_id" , db.Integer , db.ForeignKey("users.id")),
    db.Column("role_id" , db.Integer , db.ForeignKey("roles.id"))
)

from .user import User
from .role import Role
from .appointment import Appointment
from .doctor import Doctor
from .department import Department
from .patient import Patient
from .treatment import Treatment
from .availability import Availability
from .doctor_day_status import DoctorDayStatus
