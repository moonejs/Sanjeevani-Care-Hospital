from flask import Blueprint
from flask_restful import Api
from .auth import Me
from .register import PatientRegister

auth_bp=Blueprint("auth_bp",__name__)
auth_api=Api(auth_bp)

auth_api.add_resource(Me,"/me")
auth_api.add_resource(PatientRegister,"/patient/register")