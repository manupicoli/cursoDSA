#DIVIDINDO O ARQUIVO EM COLUNAS

f = open("arquivos/salarios.csv", "r")

data = f.read()

rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(',') #cada item é separado por vírgula
    full_data.append(split_row) #portanto, vai gerar uma lista separada por colunas

print(full_data) #resulta em uma lista de listas