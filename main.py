# import requests
# import json
#
# url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
# response = requests.get(url)
# print(response)
#
# if response.status_code == 200:
#     dados_json = response.json()
#     dados_restaurante = {}
#     for item in dados_json:
#         nome_do_restaurante = item['Company']
#         if nome_do_restaurante not in dados_restaurante:
#             dados_restaurante[nome_do_restaurante] = []
#
#         dados_restaurante[nome_do_restaurante].append({
#             "item": item['Item'],
#             "price": item['price'],
#             "description": item['description']
#         })
#
#
# else:
#     print(f'O erro foi {response.status_code}')
#
# for nome_do_restaurante, dados in dados_restaurante.items():
#     nome_do_arquivo = f'{nome_do_restaurante}.json'
#     with open(nome_do_arquivo, 'w') as arquivo_restaurante:
#         json.dump(dados, arquivo_restaurante, indent=4)

from fastapi import FastAPI, Query
import requests
import json
app = FastAPI()

@app.get('/api/hello')
def hello_world():
    """
    Endpoint que exibe uma mensagem incrivel do mundo da programação!

    :return:
    """
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para ver os cardápios dos restaurantes

    :param restaurante:
    :return:
    """
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    response = requests.get(url)

    if response.status_code == 200:
        dados_jason = response.json()
        if restaurante is None:
            return {'Dados':dados_jason}

        dados_restaurante = []
        for item in dados_jason:
            if item["Company"] == restaurante:
                dados_restaurante.append({
                    "item": item["Item"],
                    "price": item["price"],
                    "descricao": item["description"]
                })
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}
    else:
        return {'Erro':f"{response.status_code} - {response.text}"}


