from flask_sqlalchemy import SQLAlchemy

"""
Declaramos todas as extenções usadas aqui.
Isso é necessario para garantir que não iremos
ter dependecias ciclicas, o que derrubaria o servidor
"""

db = SQLAlchemy()