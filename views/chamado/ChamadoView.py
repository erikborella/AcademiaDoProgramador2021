from flask import Blueprint, render_template, request, flash, redirect, url_for

from datetime import date

from Forms import ChamadoForm
from models import Equipamento, ChamadoManutencao

from extensions import db

ChamadoView = Blueprint('chamado', __name__, template_folder='templates')
titulo = "Chamados"

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
    return "Chamado index"

@ChamadoView.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = ChamadoForm()
    equipamentos = Equipamento.query.all()

    if request.method == 'POST':
       
        equipamentoParaChamada = Equipamento.query.filter(Equipamento.id == form.equipamento_id.data).first()
        print(equipamentoParaChamada)

        if equipamentoParaChamada is None:
            flash("Equipamento não encontrado, selecione um valido!")
            return redirect(url_for('chamado.index'))

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
