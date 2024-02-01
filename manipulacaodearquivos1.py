arq1 = open("arquivos/arquivo1.txt", "r") #r = read

print(type(arq1))

print(arq1.read()) #lendo o conteúdo do arquivo

print(arq1.tell()) #conta o número de caracteres

print(arq1.seek(0,0)) #as coordenadas 0,0 retornam o cursor p/ o início do arquivo

print(arq1.read(23)) #Lê os primeiros 23 caracteres