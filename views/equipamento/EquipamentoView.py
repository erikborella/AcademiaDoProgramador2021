from flask import Blueprint, render_template, request, flash, redirect, url_for

from extensions import db

from Forms import RegistrarEquipamentoForm
from models import Equipamento

from datetime import date

EquipamentoView = Blueprint('equipamento', __name__, template_folder='templates')

def getDate(dataStr: str) -> date:
    datasSeparadas = dataStr.split('/')
    return date(
        int(datasSeparadas[2]), 
        int(datasSeparadas[1]), 
        int(datasSeparadas[0])
        )

@EquipamentoView.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrarEquipamentoForm()
    if request.method == 'POST':
        
        if form.validate_on_submit():
            equipamento = Equipamento(
                form.nome.data,
                form.numeroDeSerie.data,
                form.preco.data,
                getDate(form.dataDeFabricacao.data),
                form.fabricante.data
            )

            try:
                db.session.add(equipamento)
                db.session.commit()
            except:
                flash("Não foi possivel registrar esse equipamento, um erro occoreu")
                return redirect(url_for('equipamento.registrar'))

            return "a"


    else:
        return render_template('registrarEquipamento.html', form=form)