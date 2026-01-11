from flask import Blueprint
from flask_restful import Api

department_bp=Blueprint("department_bp",__name__)
department_api=Api(department_bp)

from .resources import DepartmentDetails ,DepartmentResource


department_api.add_resource(DepartmentDetails,"/departments")
department_api.add_resource(DepartmentResource,"/departments/<int:id>")