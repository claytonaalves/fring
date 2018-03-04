from core.database import db
from core.categorias.models import Categoria


class Cidade(db.Model):

    id_cidade = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), nullable=False)
    uf = db.Column(db.String(2), nullable=False)

    categorias = db.relationship(Categoria, backref='cidade', cascade='delete')

    def __init__(self, nome=None, uf=None):
        self.nome = nome
        self.uf = uf

    def __repr__(self):
        return '%s - %s' % (self.nome, self.uf)

    @property
    def serialize(self):
        return {
            'id_cidade': self.id_cidade,
            'nome': self.nome,
            'uf': self.uf
        }


def serializa(cidades):
    return [cidade.serialize for cidade in cidades]
