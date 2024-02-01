#json = java script object notation
#formato usado na web
#formato de dicionário: pares de chave-valor

import json

dict_guido = {'nome': 'Guido van Rossum',
            'linguagem': 'Python',
            'similar': ['c', 'Modula-3', 'lisp'],
            'users': 1000000}

with open('arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido)) #converte o dicionario para arquivo json

with open('arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read() #com o metodo read, grava o conteudo em 'texto'
    dados = json.loads(texto) #carrega o conteúdo de'texto' no formato json, grava em 'dados'

print(dados)
