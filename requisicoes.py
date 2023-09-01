import requests
import json

link = "https://projeto.com/"

# Inserindo dados
dados = {'anexo':'0', 'codemp': 1, 'codparc': 1, 'motorista': 12, 'numnota': 123456, 'nunota': 123456, 'razaosocial': 'Nome Parceiro'}

requisicao = requests.post(f'{link}/Entregas/.json', data=json.dumps(dados))

print(requisicao)
print(requisicao.text)


# Editando dados
dados = {'razaosocial': 'Nome Parceiro (Alterado)'}

requisicao = requests.patch(f'{link}/Entregas/{'''***ID da entrega***'''}/.json', data=json.dumps(dados))

print(requisicao)
print(requisicao.text)


# Buscando dados
requisicao = requests.get(f'{link}/Entregas/.json')

dic_requisicao = requisicao.json()

#print(dic_requisicao)

#print(dic_requisicao['32584'])

for id_entrega in dic_requisicao:
    motorista = dic_requisicao[id_entrega]['motorista']

    if motorista == 12:
        print(id_entrega)

# Deletando dados
requisicao = requests.delete(f'{link}/Entregas/{'''***ID da entrega***'''}/.json')

print(requisicao)
print(requisicao.text)