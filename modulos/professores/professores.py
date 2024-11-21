from flask import Blueprint, render_template, request, redirect, flash
from models import Professor
from database import db

bp_professor = Blueprint('professores', __name__, template_folder="templates")

@bp_professor.route('/')
def index():
    dados = Professor.query.all()
    return render_template('professor.html', professores = dados)

@bp_professor.route('/add')
def add():
    return render_template('professores_add.html')

@bp_professor.route('/save', methods=['POST'])
def save():
    nome_professor = request.form.get('nome_professor')
    departamento = request.form.get('departamento')
    if nome_professor and departamento:
        bd_professor = Professor(nome_professor, departamento)
        db.session.add(bd_professor)
        db.session.commit()
        flash('Professor salvo com sucesso!!')
        return redirect('/professores')
    else:
        flash('Preencha todos os campos!!')
        return redirect('/professores/add')
