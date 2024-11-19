from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'StRiNgQNgMSaBe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/crud_flask3bim"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Professores, Disciplinas
db.init_app(app)
migrate = Migrate(app, db)

from modulos.professores.professores import bp_professor
app.register_blueprint(bp_professor, url_prefix='/professores')

from modulos.disciplinas.disciplinas import bp_disciplina
app.register_blueprint(bp_disciplina, url_prefix='/disciplinas')

@app.route("/")
def index():
    return render_template('index.html')



