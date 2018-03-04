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
    publicado       = db.Column(db.Boolean, unique=False, default=False)
    anunciante      = db.relationship('Anunciante')
    imagens         = db.relationship('ImagemPublicacao', cascade='delete')


    def add_image(self, image_filename):
        image = ImagemPublicacao()
        image.guid_publicacao = self.guid_publicacao
        image.caminho = image_filename
        db.session.add(image)


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
            'data_publicacao': self.data_publicacao.strftime('%Y-%m-%d %H:%M:%S'),
            'data_validade': self.data_validade.strftime('%Y-%m-%d %H:%M:%S'),
            'publicado': self.publicado,
            'anunciante': {
                'guid_anunciante': self.guid_anunciante,
                'razao_social': self.anunciante.razao_social,
                'nome_fantasia': self.anunciante.nome_fantasia,
                'logradouro': self.anunciante.logradouro,
                'numero': self.anunciante.numero,
                'telefone': self.anunciante.telefone,
                'celular': self.anunciante.celular,
                'email': self.anunciante.email,
                'id_categoria': self.anunciante.id_categoria
            },
            'imagens': [imagem.caminho for imagem in self.imagens]
        }


class ImagemPublicacao(db.Model):

    __tablename__ = 'publicacao_imagem'

    guid_imagem     = db.Column(db.String(36), primary_key=True)
    guid_publicacao = db.Column(db.String(36), db.ForeignKey('publicacao.guid_publicacao', ondelete='CASCADE'), nullable=False)
    caminho         = db.Column(db.String(64))


    def __init__(self):
        self.guid_imagem = str(uuid.uuid1())


    def __repr__(self):
        return '<ImagemPublicacao: %s>' % (self.caminho)

