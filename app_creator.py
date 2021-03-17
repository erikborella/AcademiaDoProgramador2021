from flask import Flask

from extensions import db

"""
Configura todas as dependencias e telas necessarias do servidor
"""

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_pyfile('config.py')

    register_blueprint(app)
    register_extensions(app)

    return app

# Registra as telas
def register_blueprint(app: Flask):
    pass

# Registra as dependencias
def register_extensions(app):
    db.init_app(app)