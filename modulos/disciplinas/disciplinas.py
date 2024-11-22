from flask import Blueprint, render_template, request, redirect, flash
from models import Disciplina, Professor
from database import db

bp_disciplina = Blueprint('disciplinas', __name__, template_folder="templates")

@bp_disciplina.route('/')
def index():
    dados = Disciplina.query.all()
    return render_template('disciplina.html', disciplinas = dados)

@bp_disciplina.route('/add')
def add():
    p = Professor.query.all()
    return render_template('disciplina_add.html', professores = p)

@bp_disciplina.route('/save', methods=['POST'])
def save():
    professor_id = request.form.get('professor_id')
    disciplina = request.form.get('disciplina')
    credito = request.form.get('credito')
    if professor_id and disciplina and credito:
        bd_disciplina = Disciplina(professor_id, disciplina, credito)
        db.session.add(bd_disciplina)
        db.session.commit()
        flash('Disciplina salva com sucesso!!')
        return redirect('/disciplinas')
    else:
        flash('Preencha todos os campos!!')
        return redirect('/disciplinas/add')
