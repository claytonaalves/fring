from app import db

class Categoria(db.Model):

    id_categoria = db.Column(db.Integer, primary_key=True)
    id_cidade    = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    descricao    = db.Column(db.Text, nullable=False)
    imagem       = db.Column(db.Text)

    anunciantes  = db.relationship('Anunciante', backref='categoria')

    def __init__(self, descricao, cidade):
        self.descricao = descricao
        self.cidade = cidade

    def __repr__(self):
        return '<Categoria: %s>' % (self.descricao)                    

