#coding: utf8
import datetime
import requests
import uuid
import time

def cria_publicacao(titulo, descricao):
    hoje = datetime.datetime.now()
    payload = {
        "guid_publicacao": str(uuid.uuid4()),
        "guid_anunciante": "3410b388-4f21-449e-87d1-186af2b5f206",
        "id_categoria": 7,
        "titulo": titulo,
        "descricao": descricao,
        "data_publicacao": hoje.strftime("%s"),
        "data_validade": (hoje + datetime.timedelta(days=1)).strftime("%s"),
    }
    r = requests.post("http://localhost:5000/publicacoes/", json=payload)

    print(r)
    print(r.text)

#cria_publicacao("É hora da pizza", "Toda quarta e quinta delicioso rodízio de pizzas no Divina Pizza.")
#cria_publicacao("Construções e Acabamentos", "Construções e Acabamentos é na Beira Rio")
#cria_publicacao("Robertinho motos", "Atendimento rápido, Peças e Qualidade nos serviços prestados.")
cria_publicacao("Buffet para eventos em Geral", "Buffet para Casamentos, Aniversários, Confraternizações, etc...")

