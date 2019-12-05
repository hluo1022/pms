from flask import jsonify
from flask import Blueprint
from flask_restplus import Resource
from ..restplus import api
from flask_restplus import fields

blueprint = Blueprint('routes', __name__)

ns = api.namespace('routes', description='Operations related to pms posts')

task = {
    'id': 1,
    'title': 'Buy groceries',
    'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
}

task_model = api.model('test', {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
})

@ns.route('/')
class Routes(Resource):

    @api.response(204, 'Successful')
    @api.marshal_with(task_model)
    def get(self):
        return task

@blueprint.route('/')
def index():
    return "Hello, World!"