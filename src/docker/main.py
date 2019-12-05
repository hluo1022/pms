from app import settings
from app.endpoints import routes
from app.restplus import api
from flask import Flask

app = Flask(__name__)

def configure_app():
    app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION

    app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app():
	configure_app()

	api.init_app(routes.blueprint)
	api.add_namespace(routes.ns)

	app.register_blueprint(routes.blueprint)

initialize_app()