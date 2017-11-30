from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import BaseConfig

from core.database import db
from core.cidades.models import Cidade
from core.anunciantes.models import Anunciante
from core.device.models import Device
from core.publicacoes.models import Publicacao
from core.categorias.models import Categoria

app = Flask(__name__)
app.config.from_object(BaseConfig)

db.init_app(app)
migrate = Migrate(app, db)
