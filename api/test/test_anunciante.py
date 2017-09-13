#coding: utf8
import datetime
import requests
import uuid

def cria_anunciante(id_categoria, nome_fantasia, telefone, endereco):
    hoje = datetime.datetime.now()
    payload = {
        "guid_anunciante": str(uuid.uuid4()),
        "id_cidade": 1,
        "id_categoria": id_categoria,
        "nome_fantasia": nome_fantasia,
        "endereco": endereco,
        "numero": "1234",
        "bairro": "Centro",
        "telefone": telefone,
        "celular": "",
        "email": "",
    }
    r = requests.post("http://localhost:5000/anunciantes/", json=payload)

    print(r)
    print(r.text)

cria_anunciante(1, "Divina Pizza", "(66) 3521-6666", "Rua D")


