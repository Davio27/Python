# Pegar Informações - GET

import requests
requisicao = requests.get(link)
print(requisicao)
print(requisicao.json())

# Criar informação - POST

data = 'dicionario_python'
requisicao = requests.post(link, data=data)
print(requisicao)
print(requisicao.json())

# Editar informação - PATCH

data = 'dicionario_python'
requisicao = requests.patch(link, data=data)
print(requisicao)
print(requisicao.json())


# Deletar Informação - DELETE

requisicao = requests.delete(link)
print(requisicao)
print(requisicao.json())