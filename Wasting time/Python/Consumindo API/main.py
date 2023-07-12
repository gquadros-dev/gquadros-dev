import requests
import json


def request(URL, moeda):
    response = requests.get(URL)
    try:
        if response.status_code == 200:
            data = json.loads(response.content)
            data = data[f'{moeda}']
            return data['bid']
        else:
            return f'Erro na requisição. Código de status: {response.status_code}'
    except:
        print('Erro na requisição, verifique sua request!')

response = request('https://economia.awesomeapi.com.br/last/GBP-BRL', 'GBPBRL')


print(response) 
