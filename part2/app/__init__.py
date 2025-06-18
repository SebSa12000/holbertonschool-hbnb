from flask import Flask
from flask_restx import Api
from app.api.v1.amenities import api as amenities_ns


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', doc='/api/v1/',
              description='HBnB Application API')

    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    return app