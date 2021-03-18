from extensions import db

from datetime import date

"""
Aqui definimos como as tabelas do banco de dados serão
"""

# Modelo dos equipamentos
class Equipamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False)
    numero_de_serie = db.Column(db.String(100), nullable=False)
    preco_aquisisao = db.Column(db.Float, nullable=False)
    data_fabricacao = db.Column(db.Date, nullable=False)
    fabricante = db.Column(db.String(100), nullable=False)

    def __init__(self, nome: str, numero_de_serie: str, preco_aquisisao: float, data_fabricacao: date, fabricante: str):
        self.nome = nome
        self.numero_de_serie = numero_de_serie
        self.preco_aquisisao = preco_aquisisao
        self.data_fabricacao = data_fabricacao
        self.fabricante = fabricante

    def __repr__(self):
        return "<Equipamento: %r:%r>" % (self.nome, self.preco_aquisisao)

# Modelo das chamadas de manutenção
class ChamadoManutencao(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)

    equipamento_id = db.Column(db.String(100), db.ForeignKey('equipamento.id'), nullable=False)
    equipamento = db.relationship('Equipamento', backref=db.backref('chamados', lazy=True))

    data_de_abertura = db.Column(db.Date, nullable=False)

    def __init__(self, titulo: str, descricao: str, equipamento: Equipamento, data_de_abertura: date):
        self.titulo = titulo
        self.descricao = descricao
        self.equipamento = equipamento
        self.data_de_abertura = data_de_abertura

    def __repr__(self):
        return "<Chamada %r:%r>" % (self.titulo, self.equipamento)