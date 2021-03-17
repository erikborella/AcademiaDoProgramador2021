from flask import Flask

from extensions import db

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_pyfile('config.py')

    register_blueprint(app)
    register_extensions(app)

    return app

def register_blueprint(app: Flask):
    pass

def register_extensions(app: Flask):
    pass