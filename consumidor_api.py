from pprint import pprint
import requests


while True:
    try:
        lat = float(input("Insira a Latitude"))
        long = float(input("Insira a Longitude: "))
        break
    except Exception as erro:
        print("Erro, cordenada desconhecida.")
        

def consulta_tempo():

    API_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m"

    resposta = requests.get(
        API_url,
        params = [
            lat,
            long
        ],
        timeout = 15
        )
        
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