import requests
import json

response = requests.get('https://economia.awesomeapi.com.br/last/GBP-BRL')

if response.status_code == 200:
    data = response.json()
else:
    print('Erro na requisição. Código de status: {response.status_code}')

data = str(data)

json_data = json.loads(data)

print(json_data["high"])

