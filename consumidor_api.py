# IMPORT DAS BIBLIOTECAS E SUAS FUNÇÕES
from pprint import pprint
import requests

#WHILE PARA REPETIÇÃO DA PERGUNTA EM CASO DE ERRO 
while True:
    try:
        lat = float(input("Insira a Latitude"))
        long = float(input("Insira a Longitude: "))
        break
    except Exception as erro:
        print("Erro, cordenada desconhecida.")
        
#FUNÇÃO DO PROGRAMA CUNSULTA_TEMPO
def consulta_tempo():
    
    #URL DA API
    API_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m"

    #REQUISIÇÃO DA RESPOSTA 
    resposta = requests.get(
        API_url,
        params = [
            lat,
            long
        ],
        timeout = 15
        )

    #VERIFICANDO O STATUS DA RESPOSTA E O QUE ELA RETORNOU    
    resposta.raise_for_status()
    dados = resposta.jason()

    if dados == 200:
        print('Requisição cuncluida')
        pprint(dados)

    elif dados == 400:
        print('Bad request')
        pprint(dados)

    elif dados == 401:
        print('Unauthorized')
        pprint (dados)

    elif dados == 403:
        print('Forbidden')
        pprint(dados)

    elif dados == 404:
        print("Not found")
        pprint(dados)

    elif dados == 429:
        print("To many requests")
        pprint(dados)

    else:
        print("Falha no servidor")