#coding: utf8
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField
from wtforms.validators import DataRequired, Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from core.database import db
from core.cidades.models import Cidade

def cidades_choices():
    return db.session.query(Cidade).all()

class CadastroForm(FlaskForm):
    nome_fantasia = TextField(u"Nome Fantasia", validators=[DataRequired(message=u"Este campo é obrigatório")])
    razao_social = TextField(u"Razão Social")
    telefone = TextField(u"Telefone")
    celular = TextField(u"Celular")
    logradouro = TextField(u"Rua")
    numero = TextField(u"Número")
    bairro = TextField(u"Bairro")
    email = TextField(u"E-mail")
    senha = PasswordField(u"Senha")
    cidade = QuerySelectField(u'Cidade', query_factory=cidades_choices)
    categoria = SelectField(u'Categoria', choices=[('1', u'Oficina'), ('2', u'Imobiliárias')])


