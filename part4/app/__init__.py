from flask import Flask
from flask_restx import Api
from config import config
from flask_jwt_extended import JWTManager
from app.extensions import db
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.users import api as users_ns
from app.api.v1.reviews import api as review_ns
from app.api.v1.auth import api as auth_ns
from app.extension_bcrypt import bcrypt

jwt = JWTManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    jwt.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)

    api = Api(app, version='1.0', title='HBnB API', doc='/api/v1/',
              description='HBnB Application API')

    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(review_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')

    return app
