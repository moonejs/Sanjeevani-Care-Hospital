from flask import Blueprint
from flask_restful import Api

patient_bp = Blueprint("patient_bp",__name__)
patient_api = Api(patient_bp)

from .resources import PatientList 

patient_api.add_resource(PatientList,"/patients")