from flask_restplus import Resource, Namespace, fields

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

@api.route('/')
class Routes(Resource):

    @api.response(200, 'Successful')
    @api.marshal_with(task_model)
    def get(self):
        return task