import os
import logging
import uuid

from flask import Blueprint, request, render_template, session, redirect, url_for
from flask import current_app

# from werkzeug import check_password_hash, generate_password_hash
# from werkzeug.utils import secure_filename
from flask_simplelogin import login_required

from core.database import db
from core.anunciantes.models import Anunciante
from core.publicacoes.models import Publicacao
from app.publicacoes.forms import PublicacaoForm

publicacoes_blueprint = Blueprint('publicacoes', __name__)


@publicacoes_blueprint.app_template_filter()
def formata_data(value):
    return value.strftime("%d/%m/%Y")


@publicacoes_blueprint.route('/', methods=['GET'])
@login_required
def index_publicacoes():
    guid_anunciante = session.get('guid_anunciante')
    publicacoes = Publicacao.query.filter_by(guid_anunciante=guid_anunciante)
    return render_template("publicacoes/index.html", publicacoes=publicacoes)


@publicacoes_blueprint.route('/nova', methods=['GET', 'POST'])
@login_required
def nova_publicacao():
    guid_anunciante = session.get('guid_anunciante')
    anunciante = Anunciante.query.filter_by(guid_anunciante=guid_anunciante).first()
    form = PublicacaoForm()
    if form.validate_on_submit():
        salva_publicacao(anunciante, form)
        return redirect(url_for('publicacoes.index_publicacoes'))
    else:
        print(form.errors)
    return render_template('publicacoes/nova.html', form=form, anunciante=anunciante)


@publicacoes_blueprint.route('/exclui/<guid_publicacao>', methods=['GET', 'POST'])
@login_required
def exclui_publicacao(guid_publicacao):
    publicacao = Publicacao.query.filter_by(guid_publicacao=guid_publicacao).first()
    if request.method == 'GET':
        form = PublicacaoForm(obj=publicacao)
        return render_template('publicacoes/exclui.html', publicacao=publicacao, form=form)
    else:
        db.session.delete(publicacao)
        db.session.commit()
        return redirect(url_for('publicacoes.index_publicacoes'))


@publicacoes_blueprint.route('/edita/<guid_publicacao>', methods=['GET', 'POST'])
@login_required
def edita_publicacao(guid_publicacao):
    publicacao = Publicacao.query.filter_by(guid_publicacao=guid_publicacao).first()
    if request.method == 'GET':
        form = PublicacaoForm(obj=publicacao)
        return render_template('publicacoes/edita.html', publicacao=publicacao, form=form)
    else:
        form = PublicacaoForm()
        form.populate_obj(publicacao)
        db.session.add(publicacao)
        db.session.commit()
        return redirect(url_for('publicacoes.index_publicacoes'))


def salva_publicacao(anunciante, form):
    logging.info('Salvando publicacao')
    nome_arquivo_imagem = salva_imagem()
    publicacao = Publicacao()
    publicacao.guid_anunciante = anunciante.guid_anunciante
    publicacao.id_categoria = anunciante.id_categoria
    publicacao.imagem = nome_arquivo_imagem
    form.populate_obj(publicacao)
    db.session.add(publicacao)
    db.session.commit()


def salva_imagem():
    if 'imagem' not in request.files:
        return ''
    arquivo = request.files['imagem']
    if arquivo.filename == '':
        return ''
    if arquivo and allowed_file(arquivo.filename):
        filename, extension = os.path.splitext(arquivo.filename)
        filename = str(uuid.uuid4()) + extension
        arquivo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return filename


def allowed_file(filename):
    return True
