import uuid

from core.database import db

class Publicacao(db.Model):

    guid_publicacao = db.Column(db.String(36), primary_key=True)
    guid_anunciante = db.Column(db.String(36), db.ForeignKey('anunciante.guid_anunciante'), nullable=False)
    id_categoria    = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'), nullable=False)
    titulo          = db.Column(db.Text, nullable=False)
    descricao       = db.Column(db.Text, nullable=False)
    data_publicacao = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    data_validade   = db.Column(db.DateTime, nullable=False)
    imagem          = db.Column(db.String(64))
    publicado       = db.Column(db.Boolean, unique=False, default=False)

    def __init__(self):
        self.guid_publicacao = str(uuid.uuid1())

    def __repr__(self):
        return '<Publicacao: %s>' % (self.titulo)                    

    @property
    def serialize(self):
        return {
            'guid_publicacao': self.guid_publicacao,
            'guid_anunciante': self.guid_anunciante,
            'id_categoria': self.id_categoria,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'data_publicacao': self.data_publicacao,
            'data_validade': self.data_validade,
            'imagem': self.imagem,
            'publicado': self.publicado,
        }

