from flask_restplus import Resource, Namespace, fields
from ..stores import client

api = Namespace('routes', description='Operations related to pms posts')

task_model = api.model('test', {
    'id': fields.Integer(description='Id'),
    'title': fields.String(description='Title'),
    'description': fields.String(description='Desc'),
})

task = {
    'id': 1,
    'title': 'Buy groceries',
    'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
}

@api.route('/test')
class Routes(Resource):

    @api.response(200, 'Successful')
    @api.marshal_with(task_model)
    def get(self):
        return task

    @api.response(200, 'Successful')
    @api.expect(task_model)
    @api.marshal_with(task_model, code=201)
    def post(self):
        client.mkdir('test')
        client.mkdir('test/test1')
        client.cd('test')
        print(client.cwd())
        print(client.ls())
        client.rm('test1')
        client.cd('/')
        print(client.ls())
        return task, 201
