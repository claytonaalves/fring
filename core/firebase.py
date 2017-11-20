import urllib3
urllib3.disable_warnings()

import requests

from .settings import settings

FIREBASE_API_KEY = settings["firebase_api_key"]


#def publica_anuncio_firebase(anuncio):
#    print(anuncio)


def publica_anuncio_firebase(publicacao, topic="/topics/global"):
    message = {
        "to": topic,
        "data": {
            "guid_publicacao": publicacao.guid_publicacao,
            "titulo": publicacao.titulo,
            "descricao": publicacao.descricao,
        },
        "notification": {
            "title": publicacao.titulo,
            "body": publicacao.descricao,
            # "icon" : "myicon"
            "click_action": "ACTION_NOVO_ANUNCIO",
        }
    }

    headers = {
        'Content-type': 'application/json',
        'Authorization': 'key=' + FIREBASE_API_KEY
    }
    r = requests.post('https://fcm.googleapis.com/fcm/send',
                      json=message, headers=headers, verify=False)
    return r.text


if __name__ == "__main__":
    import datetime

    class Publicacao():
        pass

    publicacao = Publicacao()
    publicacao.guid_publicacao = "teste-abcd-210903"
    publicacao.titulo = "Anuncio" + datetime.datetime.now().strftime('%H:%M:%S')
    publicacao.descricao = "Grande oferta imperdivel 210903"

    r = publica_anuncio_firebase(publicacao)
    print(r)

