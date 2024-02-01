#Gravação de arquivos = SOBRESCREVENDO O ARQUIVO

arq2 = open("arquivos/arquivo2.txt", "w") # w = write
#se não houver arquivo2, ele vai criar o arquivo, se já existir ele vai sobrescrever o arquivo

arq2.write('Aprendendo a programar em Python.')

arq2.close()

arq2 = open("arquivos/arquivo2.txt", "r")

print(arq2.read())