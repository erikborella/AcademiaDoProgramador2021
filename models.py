
from extensions import db

class Equipamento(db.Model):
    numeroDeSerie = db.Column(db.String(100), primary_key=True)

    nome = db.Column(db.String(100), nullable=False)
    precoAquisisao = db.Column(db.Float, nullable=False)
    dataFabricacao = db.Column(db.Date, nullable=False)
    fabricante = db.Column(db.String(100), nullable=False)

    def __init__(self, numeroDeSerie: str, nome: str, precoAquisisao: float, dataFabricacao, fabricante: str):
        self.nome = nome
        self.numeroDeSerie = numeroDeSerie
        self.precoAquisisao = precoAquisisao
        self.dataFabricacao = dataFabricacao
        self.fabricante = fabricante

    def __repr__(self):
        return "<Equipamento: %r:%r>" % (self.nome, self.precoAquisisao)