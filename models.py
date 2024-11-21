from database import db

class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key = True)
    nome_professor = db.Column(db.String(100))
    departamento = db.Column(db.String(50))

    def __init__(self, nome, departamento):
        self.nome = nome
        self.departamento = departamento

    def __repr__(self):
        return "<Professor {self.nome}>".f
    

class Disciplina(db.Model):
    __tablename__ = 'disciplina'
    id = db.Column(db.Integer, primary_key = True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    nome_disciplina = db.Column(db.String(100))
    credito = db.Column(db.Integer)

    usuario = db.relationship('Professor', foreign_keys=professor_id)

    def __init__(self, professor_id, nome_disciplina, credito):
        self.professor_id = professor_id
        self.nome_disciplina = nome_disciplina
        self.credito = credito

    def __repr__(self):
        return "<Disciplina {self.professor.nome} - {self.disciplina.nome_disciplina} - {self.credito}>".f