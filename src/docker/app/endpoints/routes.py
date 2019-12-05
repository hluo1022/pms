from flask import jsonify
from flask import Blueprint
from flask_restplus import Resource
from ..restplus import api
from .. import models

blueprint = Blueprint('routes', __name__)

ns = api.namespace('routes', description='Operations related to pms posts')

task = {
    'id': 1,
    'title': 'Buy groceries',
    'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
}

@ns.route('/')
class Routes(Resource):

    @api.response(200, 'Successful')
    @api.marshal_with(models.task_model)
    def get(self):
        return task

@blueprint.route('/')
def index():
    return "Hello, World!"