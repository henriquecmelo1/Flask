from src import db
from datetime import datetime

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    data = db.Column(db.DateTime, default=datetime.now())
    assunto = db.Column(db.String(100))
    mensagem = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Contato %r>' % self.nome