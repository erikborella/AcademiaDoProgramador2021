from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, Length

class RegistrarEquipamentoForm(FlaskForm):

    nome = StringField('nome', validators=[DataRequired(), Length(min=6)])
    preco = FloatField('preco', validators=[DataRequired()])
    numeroDeSerie = StringField('numeroDeSerie', validators=[DataRequired()])
    dataDeFabricacao = StringField('dataDeFabricacao', validators=[DataRequired()])
    fabricante = StringField('fabricante', validators=[DataRequired()])