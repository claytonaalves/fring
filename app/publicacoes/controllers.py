import logging

from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from werkzeug import check_password_hash, generate_password_hash
from flask_simplelogin import login_required

from app import db
from app.anunciantes.models import Anunciante
from app.publicacoes.models import Publicacao
from app.publicacoes.forms import PublicacaoForm

blueprint = Blueprint('publicacoes', __name__, url_prefix='/publicacoes')

@blueprint.route('/', methods=['GET'])
@login_required
def index():
    guid_anunciante = session.get('guid_anunciante')
    publicacoes = Publicacao.query.filter_by(guid_anunciante=guid_anunciante)
    return render_template("publicacoes/index.html", publicacoes=publicacoes)

@blueprint.route('/nova', methods=['GET', 'POST'])
@login_required
def nova():
    guid_anunciante = session.get('guid_anunciante')
    anunciante = Anunciante.query.filter_by(guid_anunciante=guid_anunciante).first()
    form = PublicacaoForm()
    if form.validate_on_submit():
        salva_publicacao(anunciante, form)
        return redirect('/')
    else:
        print(form.errors)
    return render_template('publicacoes/nova.html', form=form, anunciante=anunciante)

def salva_publicacao(anunciante, form):
    logging.info('Salvando publicacao')
    publicacao = Publicacao()
    publicacao.guid_anunciante = anunciante.guid_anunciante
    publicacao.id_categoria = anunciante.id_categoria
    form.populate_obj(publicacao)
    db.session.add(publicacao)
    db.session.commit()

@blueprint.app_template_filter()
def formata_data(value):
    return value.strftime("%d/%m/%Y")
