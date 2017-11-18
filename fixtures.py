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
        ("Advogados", "advogados.png"),
        ("Agronegócio", "agronegocios.png"),
        ("Aluguel", "aluguel.png"),
        ("Automóveis", "car.png"),
        ("Beleza e Bem-estar", "beleza.png"),
        ("Carros e motos", "car.png"),
        ("Caça e pesca", "peixe.png"),
        ("Construção", "construcao.png"),
        ("Decoração e Presentes", "presente.png"),
        ("Dentistas", "dente.png"),
        ("Diversos", "placeholder.png"),
        ("Escolas", "escola.png"),
        ("Escritórios Despachante", "construcao.png"),
        ("Eventos", "eventos.png"),
        ("Farmácias", "farmacia.png"),
        ("Hospital e Clínicas", "hospital.png"),
        ("Hotéis e Agências de Turismo", "hoteis.png"),
        ("Imóveis", "imoveis.png"),
        ("Informática", "computador.png"),
        ("Médicos", "medico.png"),
        ("Móveis e Eletrônicos", "moveis.png"),
        ("Outras modalidades", "placeholder.png"),
        ("Padarias e Pizzarias", "pizza.png"),
        ("Papelarias e Armarinhos", "paperclamp.png"),
        ("Petshops", "dog.png"),
        ("Restaurantes", "restaurante.png"),
        ("Supermercados e Mercearias", "mercado.png"),
        ("Telefones úteis", "telefone.png"),
        ("Táxi", "taxi.png"),
        ("Vestuário e Calçados", "roupa.png"),
    ]

    for cidade in cidades:
        db.session.add(cidade)
    db.session.commit()

    for cidade in cidades:
        for c in categorias:
            categoria = Categoria(c[0], cidade, c[1])
            db.session.add(categoria)
        db.session.commit()
