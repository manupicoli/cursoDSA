#DIVIDINDO EM LINHA ÚNICA
f = open("arquivos/salarios.csv", "r")

data = f.read() #guarda o conteúdo dentro da varivel data

rows = data.split('\n') #separa sempre que encontrar enter, gerando uma lista

print(rows) 