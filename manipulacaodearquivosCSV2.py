import csv

#gerando uma lista
with open('arquivos/numeros.csv', 'r', encoding='utf8', newline= '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

#para não printar o cabeçalho
for linha in dados[1:]:
    print(linha)