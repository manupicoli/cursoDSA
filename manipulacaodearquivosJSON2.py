from urllib.request import urlopen #para abrir arquivos da web
import json

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print ('Título: ', dados['title'])
print ('URL: ', dados['url'])
print ('Duração: ', dados['duration'])
print ('Número de Visualizações: ', dados['stats_number_of_plays'])

#para copiar o conteúdo de um arquivo para outro:

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/dados.txt'

#with dentro de with:
with open(arquivo_fonte, 'r') as infile:
    text = infile.read() #vai ler o arquivo
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text) #gravando o conteudo do primeiro arquivo lido

#para simplificar
open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())

#para ler
with open('arquivos/dados.txt', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)