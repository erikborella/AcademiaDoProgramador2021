import sys
from functools import wraps

from main import app
from extensions import db

from sqlalchemy import create_engine

""" Importe todos os modelos aqui para fazer a migração """
from models import Equipamento, ChamadaManutencao


""" Decorator para ser usado fora do serviço do Flask """
def with_app_context(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        with app.app_context():
            f(*args, **kwargs)
    return decorated


""" Deleta e depois cria todas as tabelas """
@with_app_context
def migrate():
    db.drop_all()
    db.create_all()


""" Imprime uma lista com todos os nomes das tabelas """
@with_app_context
def show_tables():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    tables: list = engine.table_names()

    print("-------------TABLES-------------")

    for table in tables:
        print(table)

    print("--------------------------------")


""" Cria uma CLI simples para algumas funções do BD
    Use -m or --migrate para migrar o BD
    -t or --tables para mostrar todas as tabelas"""
if __name__ == "__main__":

    if '--migrate' in sys.argv or '-m' in sys.argv:
        migrate()

    if '--tables' in sys.argv or '-t' in sys.argv:
        show_tables()