from flask import Flask

from views.equipamento.EquipamentoView import EquipamentoView
from views.chamado.ChamadoView import ChamadoView

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
    app.register_blueprint(EquipamentoView, url_prefix="/equipamentos")
    app.register_blueprint(ChamadoView, url_prefix="/chamados")

# Registra as dependencias
def register_extensions(app):
    db.init_app(app)