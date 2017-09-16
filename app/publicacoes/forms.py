# encoding: utf8
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, DateField


class PublicacaoForm(FlaskForm):
    titulo = TextField(u'Título')
    descricao = TextAreaField(u'Descrição')
    data_validade = DateField(format='%d/%m/%Y')
