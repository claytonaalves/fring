import requests

URL = "http://localhost:5000"

def testa_cadastro_anunciante():
    anunciante = {
        "nome"         : "Anunciante de Teste",
        "endereco"     : "Rua xxx",
        "numero"       : "1234",
        "bairro"       : "Centro",
        "cidade"       : "Alta Floresta",
        "estado"       : "MT",
        "telefone"     : "(66) 3521-1133",
        "celular"      : "(66) 99233-3406",
        "email"        : "clayton.aa@gmail.com",
        "id_categoria" : "1",
        "guid"         : "guid-de-teste",
    }
    r = requests.post(URL + "/anunciante", json=anunciante)
    print(r)

def testa_postagem_anuncio():
    anuncio = {
        "guid": "guid-anuncio-teste-05",
        "titulo": "Anuncio de teste 05",
        "descricao": "Teste de anuncio 05",
        "valido_ate": "2017-05-26 00:00:00",
        "id_categoria": "1",
        "guid_anunciante": "3b759968-7613-41b6-be3d-4799eae4352e",
    }
    r = requests.post(URL + "/anuncio", json=anuncio)
    print(r)

if __name__=="__main__":
    testa_postagem_anuncio()
