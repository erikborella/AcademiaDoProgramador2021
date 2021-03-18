from flask import Blueprint, render_template, request, flash, redirect, url_for

from datetime import date, datetime, timedelta

from Forms import ChamadoForm
from models import Equipamento, ChamadoManutencao

from extensions import db

ChamadoView = Blueprint('chamado', __name__, template_folder='templates')
titulo = "Manutenções"

# Recebe uma string no formato dd/mm/yyyy e retorna um objeto date com a data
def getDate(dataStr: str) -> date:
    datasSeparadas = dataStr.split('/')
    return date(
        int(datasSeparadas[2]), 
        int(datasSeparadas[1]), 
        int(datasSeparadas[0])
        )


@ChamadoView.route('/')
def index():
    chamados = ChamadoManutencao.query.all()

    dataHoje = date.today()
    for chamado in chamados:
        dataDiferenca = dataHoje - chamado.dataDeAbertura
        chamado.diasAberto = dataDiferenca.days

    return render_template('chamados.html', chamados=chamados, titulo=titulo)


@ChamadoView.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = ChamadoForm()
    equipamentos = Equipamento.query.all()

    if request.method == 'POST':
       
        equipamentoParaChamada = Equipamento.query.filter(Equipamento.id == form.equipamento_id.data).first()

        if equipamentoParaChamada is None:
            flash("Equipamento não encontrado, selecione um valido!")
            return redirect(url_for('chamado.registrar'))

        chamado = ChamadoManutencao(
            form.titulo.data,
            form.descricao.data,
            equipamentoParaChamada,
            getDate(form.dataDeAbertura.data)
        )

        try:
            db.session.add(chamado)
            db.session.commit()
        except:
            flash("Não foi possivel registrar essa chamada, um erro occoreu!")
            return redirect(url_for('chamado.registrar'))
        
        return redirect(url_for('chamado.index'))

    else:
        return render_template('registrarChamado.html', equipamentos=equipamentos, form=form, titulo=titulo)


@ChamadoView.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    equipamentos = Equipamento.query.all()
    chamado: ChamadoManutencao = ChamadoManutencao.query.filter(ChamadoManutencao.id == id).first()

    if chamado is None:
        flash("Chamado com o id: %r, não foi encontrado" % (id))
        return redirect(url_for("chamado.index"))

    form = ChamadoForm()

    if request.method == 'POST' and  form.validate_on_submit():

        equipamentoParaChamada = Equipamento.query.filter(Equipamento.id == form.equipamento_id.data).first()
        if equipamentoParaChamada is None:
            flash("Equipamento não encontrado, selecione um valido!")
            return redirect(url_for('chamado.editar', id=id))

        chamado.titulo = form.titulo.data
        chamado.descricao = form.descricao.data
        chamado.equipamento = equipamentoParaChamada
        chamado.dataDeAbertura = getDate(form.dataDeAbertura.data)

        try:
            db.session.add(chamado)
            db.session.commit()
        except:
            flash("Não foi possivel editar esse chamado, um erro occoreu!")
            return redirect(url_for('chamado.editar', id=id))

        return redirect(url_for('chamado.index'))

    else:
        return render_template('editarChamado.html', chamado=chamado, equipamentos=equipamentos, form=form, titulo=titulo)


@ChamadoView.route('/excluir/<int:id>', methods=['GET'])
def excluir(id):
    chamado = ChamadoManutencao.query.filter(ChamadoManutencao.id == id).first()

    if chamado is None:
        flash("Chamado com o id: %r, não foi encontrado" % (id))
        return redirect(url_for("chamado.index"))

    try:
        db.session.delete(chamado)
        db.session.commit()
    except:
        flash("Não foi possivel excluir esse equipamento, um erro occoreu!")
        
    return redirect(url_for('chamado.index'))