from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length

"""
    Declaramos aqui quais dados são necessarios nos formulario
    E automaticamente os valida
"""


"""
    Formulario para os equipamentos
"""
class EquipamentoForm(FlaskForm):

    nome = StringField('nome', validators=[DataRequired(), Length(min=6)])
    preco = FloatField('preco', validators=[DataRequired()])
    numeroDeSerie = StringField('numeroDeSerie', validators=[DataRequired()])
    dataDeFabricacao = StringField('dataDeFabricacao', validators=[DataRequired()])
    fabricante = StringField('fabricante', validators=[DataRequired()])


"""
    Formulario para os chamados
"""
class ChamadoForm(FlaskForm):

    titulo = StringField('titulo', validators=[DataRequired()])
    descricao = StringField('descricao', validators=[DataRequired()])
    equipamento_id = IntegerField('equipamento_id', validators=[DataRequired()])
    dataDeAbertura = StringField('dataDeAbertura', validators=[DataRequired()])
    