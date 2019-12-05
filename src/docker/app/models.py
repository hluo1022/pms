from flask_restplus import fields
from .restplus import api

task_model = api.model('test', {
    'id': fields.Integer(description='Id'),
    'title': fields.String(description='Title'),
    'description': fields.String(description='Desc'),
})

