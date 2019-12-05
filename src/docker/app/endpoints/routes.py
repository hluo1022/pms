from flask import jsonify
from flask import Blueprint
from ..restplus import api

blueprint = Blueprint('routes', __name__)

ns = api.namespace('pms/posts', description='Operations related to pms posts')

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@blueprint.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@blueprint.route('/')
def index():
    return "Hello, World!"