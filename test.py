from app import db
from app.cidades.models import Cidade
from app.categorias.models import Categoria
from app.anunciantes.models import Anunciante

af = Cidade('Alta Floresta', 'MT')

db.session.add(af)
db.session.commit()

db.session.add(Categoria('Oficina', af))
db.session.commit()

db.session.add(Categoria('Escola', af))
db.session.commit()

#cat1 = Categoria.query.filter_by(id_categoria=1).first()
#an1 = Anunciante('abcd1234', 'Fulano da Oficina', cat1)
#an1.senha = '4321'
#
#db.session.add(an1)
#db.session.commit()

db.create_all()
