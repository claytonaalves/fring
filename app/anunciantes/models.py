import uuid
import datetime

from app import db

class Anunciante(db.Model):

    guid_anunciante = db.Column(db.String(36), primary_key=True)
    id_cidade       = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    id_categoria    = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'), nullable=False)
    razao_social    = db.Column(db.Text, nullable=False)
    nome_fantasia   = db.Column(db.Text, nullable=False)
    telefone        = db.Column(db.Text)
    celular         = db.Column(db.Text)
    logradouro      = db.Column(db.Text)
    numero          = db.Column(db.Text)
    bairro          = db.Column(db.Text)
    data_cadastro   = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    email           = db.Column(db.Text)
    senha           = db.Column(db.Text)

    def __init__(self, guid_anunciante=None, nome_fantasia=None, categoria=None):
        self.guid_anunciante = guid_anunciante or self.cria_novo_uuid()
        self.nome_fantasia = nome_fantasia or ''
        self.razao_social = nome_fantasia or ''
        self.data_cadastro = datetime.datetime.now()
        if categoria:
            self.id_categoria = categoria.id_categoria
            self.id_cidade = categoria.id_cidade

    def cria_novo_uuid(self):
        return str(uuid.uuid1())

    def __repr__(self):
        return '<Anunciante: %s>' % (self.nome_fantasia)                    

