from flask import Blueprint
from flask_restplus import Api

from .apis.routes import api as routes_ns

blueprint = Blueprint('api', __name__, url_prefix='api/v1')

api = Api(blueprint, version='1.0', title='PMS API',
          description='A simple demonstration of a Flask RestPlus powered API')

api.add_namespace(routes_ns)