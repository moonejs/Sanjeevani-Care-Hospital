from flask import Blueprint
from flask_restful import Api

admin_bp=Blueprint("admin_bp",__name__)
admin_api=Api(admin_bp)

