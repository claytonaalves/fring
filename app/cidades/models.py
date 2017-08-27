from app import db

class Cidade(db.Model):

    id_cidade = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), nullable=False)
    uf = db.Column(db.String(2), nullable=False)

    categorias = db.relationship('Categoria', backref='cidade')

    def __init__(self, nome, uf):
        self.nome = nome
        self.uf = uf

    def __repr__(self):
        return '<Cidade: %s - %s>' % (self.nome, self.uf)

