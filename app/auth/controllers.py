from flask import Blueprint, flash, redirect, render_template, url_for

from core.database import db
from core.cidades.models import Cidade
from core.categorias.models import Categoria
from core.anunciantes.models import Anunciante

from .forms import CadastroForm

auth_blueprint = Blueprint('auth', __name__, url_prefix='/cadastro')


@auth_blueprint.route('/', methods=['GET', 'POST'])
def auth_cadastro():
    form = CadastroForm()
    form.cidade.choices = [(cidade.id_cidade, cidade.nome) for cidade in Cidade.query.all()]
    form.categoria.choices = [(categoria.id_categoria, categoria.descricao) for categoria in Categoria.query.all()]
    if form.validate_on_submit():
        salva_cadastro_anunciante(form)
        flash('Cadastro efetuado!')
        return redirect(url_for('publicacoes.index_publicacoes'))
    return render_template('auth/cadastro.html', form=form)


def salva_cadastro_anunciante(form):
    anunciante = Anunciante()
    anunciante.nome_fantasia = form.nome_fantasia.data
    anunciante.razao_social = form.razao_social.data
    anunciante.id_cidade = form.cidade.data
    anunciante.id_categoria = form.categoria.data
    anunciante.telefone = form.telefone.data
    anunciante.celular = form.celular.data
    anunciante.logradouro = form.logradouro.data
    anunciante.numero = form.numero.data
    anunciante.bairro = form.bairro.data
    anunciante.email = form.email.data
    anunciante.senha = form.senha.data
    db.session.add(anunciante)
    db.session.commit()
