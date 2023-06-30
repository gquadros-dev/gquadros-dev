import requests
import json


def request(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        data = json.loads(response.content)
        data = data['GBPBRL.code']
        return data
    else:
        return 'Erro na requisição. Código de status: {response.status_code}'

response = request('https://economia.awesomeapi.com.br/last/GBP-BRL')


print(response) 


# response = requests.get('https://economia.awesomeapi.com.br/last/GBP-BRL')

# if response.status_code == 200:
#     data = response.json()
# else:
#     print('Erro na requisição. Código de status: {response.status_code}')

# data = str(data)

# json_data = json.loads(data)

# print(json_data["high"])
