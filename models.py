from extensions import db

from datetime import date

"""
Aqui definimos como as tabelas do banco de dados serão
"""

# Modelo dos equipamentos
class Equipamento(db.Model):
    numeroDeSerie = db.Column(db.String(100), primary_key=True)

    nome = db.Column(db.String(100), nullable=False)
    precoAquisisao = db.Column(db.Float, nullable=False)
    dataFabricacao = db.Column(db.Date, nullable=False)
    fabricante = db.Column(db.String(100), nullable=False)

    def __init__(self, numeroDeSerie: str, nome: str, precoAquisisao: float, dataFabricacao: date, fabricante: str):
        self.nome = nome
        self.numeroDeSerie = numeroDeSerie
        self.precoAquisisao = precoAquisisao
        self.dataFabricacao = dataFabricacao
        self.fabricante = fabricante

    def __repr__(self):
        return "<Equipamento: %r:%r>" % (self.nome, self.precoAquisisao)

# Modelo das chamadas de manutenção
class ChamadaManutencao(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)

    equipamento_numeroDeSerie = db.Column(db.String(100), db.ForeignKey('equipamento.numeroDeSerie'), nullable=False)
    equipamento = db.relationship('Equipamento', backref=db.backref('chamadas', lazy=True))

    dataDeAbertura = db.Column(db.Date, nullable=False)

    def __init__(self, titulo: str, descricao: str, equipamento: Equipamento, dataDeAbertura: date):
        self.titulo = titulo
        self.descricao = descricao
        self.equipamento = equipamento
        self.dataDeAbertura = dataDeAbertura

    def __repr__(self):
        return "<Chamada %r:%r>" % (self.titulo, self.equipamento)