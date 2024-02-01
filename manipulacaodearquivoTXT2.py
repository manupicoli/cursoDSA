#Para ler o arquivo

arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)