#https://viacep.com.br/ws/01001000/json/

import requests

#receiving the request from viacep's API
cep_input = input('Digite o CEP(somente numeros): ') #Input data 
request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input)) #receiving the information from viacep, using cep_input as parameter of consult
request = request.json() #update the information for json

#Data's tratative and print
print('#####################################')
if len(cep_input) != 8:
    print('cep informado diferente de 8')
    exit()
elif 'erro' in request:
    print('cep inexistente')
else:
    print('todas as informacoes: {}'.format(request))
    print('somente endereco: '.format(request['logradouro']))
