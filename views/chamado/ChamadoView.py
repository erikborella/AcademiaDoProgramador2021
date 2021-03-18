from flask import Blueprint, render_template, request, flash, redirect, url_for

from datetime import date, datetime, timedelta

from utils import converter_data_str_para_date

from forms import ChamadoForm
from models import Equipamento, ChamadoManutencao

from extensions import db

ChamadoView = Blueprint('chamado', __name__, template_folder='templates')
titulo = "Manutenções"


"""
    Pagina inicial
"""
@ChamadoView.route('/')
def index():
    chamados = ChamadoManutencao.query.all()

    dataHoje = date.today()
    for chamado in chamados:
        dataDiferenca = dataHoje - chamado.dataDeAbertura
        chamado.diasAberto = dataDiferenca.days

    return render_template('chamados.html', chamados=chamados, titulo=titulo)


# Pagina para registrar novos chamados
@ChamadoView.route('/registrar', methods=['GET', 'POST'])
def registrar():
    # Declaração do form para validar os inputs
    form = ChamadoForm()
    # Acha todos os equipamentos registrados
    equipamentos = Equipamento.query.all()

    # Registra um novo chamado
    if request.method == 'POST':
       
        # Verifica se o equipamento existe
        equipamentoParaChamada = Equipamento.query.filter(Equipamento.id == form.equipamento_id.data).first()

        # Caso não exista, coloqua uma mensagem no flash e recarregue a pagina
        if equipamentoParaChamada is None:
            flash("Equipamento não encontrado, selecione um valido!")
            return redirect(url_for('chamado.registrar'))


        # Declara um chamado com as informações do form
        chamado = ChamadoManutencao(
            form.titulo.data,
            form.descricao.data,
            equipamentoParaChamada,
            converter_data_str_para_date(form.dataDeAbertura.data)
        )

        # Tenta adicionar o chamado ao banco de dados
        try:
            db.session.add(chamado)
            db.session.commit()
        except:
            # Caso não consiga, coloca uma mensagem no flash e recarrega a pagina
            flash("Não foi possivel registrar essa chamada, um erro occoreu!")
            return redirect(url_for('chamado.registrar'))

        # Se nenhum erro occorrer, vai para a pagina inicial
        return redirect(url_for('chamado.index'))

    # Mostra a pagina para registro
    else:
        return render_template('registrarChamado.html', equipamentos=equipamentos, form=form, titulo=titulo)


"""
    Permite editar o chamado com o id passado por parametro
"""
@ChamadoView.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    # Procura todos os equipamentos registrados
    equipamentos = Equipamento.query.all()
    # Verifica se o id corresponde a algum chamado
    chamado: ChamadoManutencao = ChamadoManutencao.query.filter(ChamadoManutencao.id == id).first()

    # Caso não, coloca uma mensagem no flash e volte para a pagina inicial
    if chamado is None:
        flash("Chamado com o id: %r, não foi encontrado" % (id))
        return redirect(url_for("chamado.index"))

    # Declaração do form, para validação dos dados
    form = ChamadoForm()

    # Edita o chamado se o formulario estiver valido
    if request.method == 'POST' and  form.validate_on_submit():

        # Procura se o equipamento existe
        equipamentoParaChamada = Equipamento.query.filter(Equipamento.id == form.equipamento_id.data).first()
        # Caso não, coloca uma mensagem no flash e recarrga a pagina
        if equipamentoParaChamada is None:
            flash("Equipamento não encontrado, selecione um valido!")
            return redirect(url_for('chamado.editar', id=id))

        # Define os novos valores do chamado
        chamado.titulo = form.titulo.data
        chamado.descricao = form.descricao.data
        chamado.equipamento = equipamentoParaChamada
        chamado.dataDeAbertura = converter_data_str_para_date(form.dataDeAbertura.data)

        # Tenta editar o chamado no banco de dados
        try:
            db.session.add(chamado)
            db.session.commit()
        except:
            # Caso ocorra algum erro, coloca uma mensagem no flash e recarrega a pagina
            flash("Não foi possivel editar esse chamado, um erro occoreu!")
            return redirect(url_for('chamado.editar', id=id))

        # Caso nenuhum erro ocorra, volte para a pagina inicial
        return redirect(url_for('chamado.index'))

    # Mostra a pagina de edição
    else:
        return render_template('editarChamado.html', chamado=chamado, equipamentos=equipamentos, form=form, titulo=titulo)


"""
    Permite excluir um chamado com o id passado por parametro
"""
@ChamadoView.route('/excluir/<int:id>', methods=['GET'])
def excluir(id):
    # Procura pelo chamado com o id passado por parametro
    chamado = ChamadoManutencao.query.filter(ChamadoManutencao.id == id).first()

    # Caso não encontre, coloca uma mensagem no flash e volta para a tela incial
    if chamado is None:
        flash("Chamado com o id: %r, não foi encontrado" % (id))
        return redirect(url_for("chamado.index"))

    # Tenta deletar o chamado do banco de dados
    try:
        db.session.delete(chamado)
        db.session.commit()
    except:
        # Caso não cosiga, coloca uma mensagem no flash
        flash("Não foi possivel excluir esse equipamento, um erro occoreu!")
    
    # Volta para a tela inicial
    return redirect(url_for('chamado.index'))