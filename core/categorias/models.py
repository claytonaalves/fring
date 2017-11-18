from core.database import db

class Categoria(db.Model):

    id_categoria = db.Column(db.Integer, primary_key=True)
    id_cidade    = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    descricao    = db.Column(db.Text, nullable=False)
    imagem       = db.Column(db.Text)

    anunciantes  = db.relationship('Anunciante', backref='categoria')

    def __init__(self, descricao=None, cidade=None, imagem=None):
        self.descricao = descricao
        self.cidade = cidade
        self.imagem = imagem

    def __repr__(self):
        return '<Categoria {0}: {1}>'.format(self.id_categoria, self.descricao)                    

def serializa(categorias):
    result = []
    for categoria in categorias:
        categoria_dict = {
            'id_categoria': categoria.id_categoria,
            'descricao': categoria.descricao,
            'imagem': categoria.imagem,
            'qtde_anunciantes': len(categoria.anunciantes),
        }
        result.append(categoria_dict)
    return result
