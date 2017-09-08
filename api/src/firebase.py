import requests
import settings

FIREBASE_API_KEY = settings.settings["firebase_api_key"]

def puclica_anuncio_test(anuncio):
    print(anuncio)

def publica_anuncio(anuncio):
    message = {
        "to": "/topics/global",
        "data": {
            "guid_anuncio" : anuncio["guid"],
            "titulo"       : anuncio["titulo"],
            "descricao"    : anuncio["descricao"],
        },
        "notification" : {
          "title" : anuncio["titulo"],
          "body" : anuncio["descricao"],
          #"icon" : "myicon"
          "click_action": "ACTION_NOVO_ANUNCIO",
        }
    }

    headers = {
        'Content-type': 'application/json',
        'Authorization': 'key=' + FIREBASE_API_KEY
    }
    r = requests.post('https://fcm.googleapis.com/fcm/send', 
                      json=message, headers=headers)
    print(r.text)

if __name__=="__main__":
    anuncio = {
        "titulo": "Anuncio 1405",
        "descricao": "Grande oferta imperdivel",
        "guid": "teste-abcd-1234"
    }
    publica_anuncio(anuncio)
