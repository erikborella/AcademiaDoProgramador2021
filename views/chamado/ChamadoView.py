from flask import Blueprint

ChamadoView = Blueprint('chamado', __name__, template_folder='templates')
Titulo = "Chamados"

@ChamadoView.route('/')
def index():
    return "Chamado index"