#ACRESCENTANDO CONTEÚDO

arq2 = open("arquivos/arquivo2.txt", "a") # a = append
#Dessa forma, o arquivo não será sobrescrito, apenas vai acrescentar conteúdo

arq2.write(' E a metodologia de ensino da Data Science Academy facilita o aprendizado.')

arq2.close()

arq2 = open("arquivos/arquivo2.txt", "r")

print(arq2.read())