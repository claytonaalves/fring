# encoding: utf8
from config import ApiConfig
from core.database import db
from core.device.models import Device
from core.cidades.models import Cidade
from core.categorias.models import Categoria
from core.anunciantes.models import Anunciante
from api.app import create_app

app = create_app(ApiConfig)

with app.app_context():
    db.create_all()

    cidades = [
        Cidade('Alta Floresta','MT'),
        Cidade('Apiacás','MT'),
        Cidade('Bandeirantes','MT'),
        Cidade('Carlinda','MT'),
        Cidade('Cuiabá','MT'),
        Cidade('Guarantã do Norte','MT'),
        Cidade('Lucas do Rio Verde','MT'),
        Cidade('Matupá','MT'),
        Cidade('Monte Verde','MT'),
        Cidade('Peixoto de Azevedo','MT'),
        Cidade('Sinop','MT'),
    ]
    categorias = [
        (u"Advogados", "advogados.png"),
        (u"Agronegócio", "agronegocios.png"),
        (u"Aluguel", "aluguel.png"),
        (u"Automóveis", "car.png"),
        (u"Beleza e Bem-estar", "beleza.png"),
        (u"Carros e motos", "car.png"),
        (u"Caça e pesca", "peixe.png"),
        (u"Construção", "construcao.png"),
        (u"Decoração e Presentes", "presente.png"),
        (u"Dentistas", "dente.png"),
        (u"Diversos", "placeholder.png"),
        (u"Escolas", "escola.png"),
        (u"Escritórios Despachante", "construcao.png"),
        (u"Eventos", "eventos.png"),
        (u"Farmácias", "farmacia.png"),
        (u"Hospital e Clínicas", "hospital.png"),
        (u"Hotéis e Agências de Turismo", "hoteis.png"),
        (u"Imóveis", "imoveis.png"),
        (u"Informática", "computador.png"),
        (u"Médicos", "medico.png"),
        (u"Móveis e Eletrônicos", "moveis.png"),
        (u"Outras modalidades", "placeholder.png"),
        (u"Padarias e Pizzarias", "pizza.png"),
        (u"Papelarias e Armarinhos", "paperclamp.png"),
        (u"Petshops", "dog.png"),
        (u"Restaurantes", "restaurante.png"),
        (u"Supermercados e Mercearias", "mercado.png"),
        (u"Telefones úteis", "telefone.png"),
        (u"Táxi", "taxi.png"),
        (u"Vestuário e Calçados", "roupa.png"),
    ]

    for cidade in cidades:
        db.session.add(cidade)
    db.session.commit()

    for cidade in cidades:
        for c in categorias:
            categoria = Categoria(c[0], cidade, c[1])
            db.session.add(categoria)
        db.session.commit()
