#CSV = comma-separated values
import csv #pacote python para manipular esse tipo de arquivo

with open('arquivos/numeros.csv', 'w') as arquivo:
    #criando o objeto de gravação
    writer = csv.writer(arquivo) #chamando o pacote csv com o método writer, que vai gravar o argumento arquivo
    #isso fica armazenado no objeto writer

    #para gravar no arquivo linha a linha: metodo writerow
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63,87,92))
    writer.writerow((61,79,76))
    writer.writerow((72,64,91))

#Leitura de arquivos CSV
with open('arquivos/numeros.csv', 'r', encoding='utf8', newline= '\r\n') as arquivo:
    #cira o objeto de leitura
    leitor = csv.reader(arquivo)
    #loop para percorrer e printar cada elemento do objeto leitor (linhas)
    for x in leitor:
        print(x) #vai printar listas