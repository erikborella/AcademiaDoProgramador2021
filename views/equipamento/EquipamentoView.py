from flask import Blueprint, render_template, request, flash, redirect, url_for

from extensions import db

from forms import EquipamentoForm
from models import Equipamento

from datetime import date

from utils import calcular_diferença_dias_data_atual, converter_data_str_para_date

# Declaração do Blueprint e do seu titulo
EquipamentoView = Blueprint('equipamento', __name__, template_folder='templates')
titulo = "Equipamento"


"""
    Pagina inicial
""" 
@EquipamentoView.route('/')
def index():
    equipamentos = Equipamento.query.all()
    
    # Calcula há quantos dias os chamados de cada equipamento estão abertos
    for equipamento in equipamentos:
        for chamado in equipamento.chamados:
            chamado.dias_aberto = calcular_diferença_dias_data_atual(chamado.data_de_abertura)

    return render_template('equipamentos.html', equipamentos=equipamentos, titulo=titulo)


"""
    Pagina para registrar novos equipamentos
"""
@EquipamentoView.route('/registrar', methods=['GET', 'POST'])
def registrar():

    # Declaração do formulario, para a validação do memso
    form = EquipamentoForm()

    # Se a requisição é do tipo POST  e o formuario é valido, tente cadastrar o equipamento
    if request.method == 'POST' and form.validate_on_submit():
        
        # Declara o equipamento
        equipamento = Equipamento(
            form.nome.data,
            form.numero_de_serie.data,
            form.preco.data,
            converter_data_str_para_date(form.data_de_fabricacao.data),
            form.fabricante.data
        )

        # Tenta adicionar o equipamento ao banco de dados
        try:
            db.session.add(equipamento)
            db.session.commit()
        except:
            # Caso algum erro occora, volta para a pagina de registro com a mensagem flash
            flash("Não foi possivel registrar esse equipamento, um erro occoreu!")
            return redirect(url_for('equipamento.registrar'))

        # Se registrado com sucesso, volta para a pagina inicial
        return redirect(url_for('equipamento.index'))

    else:
        # Renderiza a pagina para registro
        return render_template('registrarEquipamento.html', form=form, titulo=titulo)


"""
    Pagina para editar um equipamento
"""
@EquipamentoView.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    # Procura pelo equipamento com a id passada na URL
    equipamento:Equipamento = Equipamento.query.filter(Equipamento.id == id).first()

    # Caso o equipamento não exista, volte para a pagina inicial mostrando um erro
    if (equipamento is None):
        flash("Equipamento com o id: %r não foi encontrado" % id) 
        return redirect(url_for('equipamento.index'))

    # Declaração do formulario, para a validação do memso
    form = EquipamentoForm()

    # Se a requisição é do tipo POST e o formulario é valido, tente editar o equipamento
    if request.method == 'POST' and form.validate_on_submit():

        # Seta as novas informações
        equipamento.nome = form.nome.data
        equipamento.preco_aquisisao = form.preco.data
        equipamento.data_fabricacao = converter_data_str_para_date(form.data_de_fabricacao.data)
        equipamento.numero_de_serie = form.numero_de_serie.data
        equipamento.fabricante = form.fabricante.data

        # Tenta adicionar ao banco de dados
        try:
            db.session.add(equipamento)
            db.session.commit()
        except:
            # Caso algum erro occora, volta para a pagina de edição com a mensagem flash
            flash("Não foi possivel editar esse equipamento, um erro occoreu!")
            return redirect(url_for('equipamento.editar', id=id))

        # Caso nenhum erro ocorra, volte para a pagina inicial
        return redirect(url_for('equipamento.index'))
        
    else:
        # Renderiza o template para editar o equipamento
        return render_template('editarEquipamento.html', equipamento=equipamento, form=form, titulo=titulo)


"""
    Rota para excluir um equipamento
"""
@EquipamentoView.route('/excluir/<int:id>', methods=['GET'])
def excluir(id):
    # Procura pelo equipamento com a id passada na URL
    equipamento:Equipamento = Equipamento.query.filter(Equipamento.id == id).first()

    # Caso o equipamento não exista, volte para a pagina inicial mostrando um erro
    if (equipamento is None):
        flash("Equipamento com o id: %r não foi encontrado" % id) 
        return redirect(url_for('equipamento.index'))

    # Tente deletar o equipamento do banco de dados
    try:
        # Deleta todos os chamados vinculados a esse equipamento antes
        for chamado in equipamento.chamados:
            db.session.delete(chamado)

        db.session.delete(equipamento)
        db.session.commit()
    except:
        # Caso algum erro occora, coloque uma mensagem flash informando isso
        flash("Não foi possivel excluir esse equipamento, um erro occoreu!")

    # Volta para a pagina inicial
    return redirect(url_for('equipamento.index'))