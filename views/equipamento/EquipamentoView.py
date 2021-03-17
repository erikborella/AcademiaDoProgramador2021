from flask import Blueprint, render_template, request, flash, redirect, url_for

from extensions import db

from Forms import EquipamentoForm
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

@EquipamentoView.route('/')
def index():
    equipamentos = Equipamento.query.all()
    return render_template('equipamentos.html', equipamentos=equipamentos)


@EquipamentoView.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = EquipamentoForm()
    if request.method == 'POST' and form.validate_on_submit():
        
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

        return redirect(url_for('equipamento.index'))

    else:
        return render_template('registrarEquipamento.html', form=form)


@EquipamentoView.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    equipamento:Equipamento = Equipamento.query.filter(Equipamento.id == id).first()

    if (equipamento is None):
        flash("Equipamento com o id: %r não foi encontrado" % id) 
        return redirect(url_for('equipamento.index'))

    form = EquipamentoForm()

    if request.method == 'POST' and form.validate_on_submit():

        equipamento.nome = form.nome.data
        equipamento.precoAquisisao = form.preco.data
        equipamento.dataFabricacao = getDate(form.dataDeFabricacao.data)
        equipamento.numeroDeSerie = form.numeroDeSerie.data
        equipamento.fabricante = form.fabricante.data

        try:
            db.session.add(equipamento)
            db.session.commit()
        except:
            flash("Não foi possivel editar esse equipamento, um erro occoreu")
            return redirect(url_for('equipamento.editar', id=id))

        return redirect(url_for('equipamento.index'))
        
    else:
        return render_template('editarEquipamento.html', equipamento=equipamento, form=form)