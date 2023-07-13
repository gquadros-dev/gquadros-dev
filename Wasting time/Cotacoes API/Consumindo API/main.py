import requests
import json

class ConverterMoedas:
    def __init__(self, parametro):
       self.parametro = parametro
       self.URL = 'http://economia.awesomeapi.com.br/json/last/'
    

    def request(self):
        response = requests.get(f'{self.URL}{self.parametro}')
        try:
            if response.status_code == 200:
                self.parametro = self.parametro.replace('-', '')
                data = json.loads(response.content)
                data = data[self.parametro]
                return data['bid']
            else:
                print(f'Erro na requisição. Cóodigo de status: {response.status_code}.')
        except:
            print('Erro na requisição, verifique sua solicitação!')

if __name__ == '__main__':
    con = ConverterMoedas('GBP-BRL')
    con.request()




# conversao = input(str('Qual conversão deseja? '))
# moeda_desejada = conversao.index('-')
# moeda_desejada = conversao[0:moeda_desejada]

# def request(URL, moeda):
#     response = requests.get(URL)
#     try:
#         if response.status_code == 200:
#             data = json.loads(response.content)
#             data = data[f'{moeda}']
#             return data['bid']
#         else:
#             return f'Erro na requisição. Código de status: {response.status_code}'
#     except:
#         print('Erro na requisição, verifique sua request!')

# response = request(f'https://economia.awesomeapi.com.br/last/{conversao}', f'{moeda_desejada}')
# print(response)

# def request(URL, moeda):
#     response = requests.get(URL)
#     try:
#         if response.status_code == 200:
#             data = json.loads(response.content)
#             data = data[f'{moeda}']
#             return data['bid']
#         else:
#             return f'Erro na requisição. Código de status: {response.status_code}'
#     except:
#         print('Erro na requisição, verifique sua request!')