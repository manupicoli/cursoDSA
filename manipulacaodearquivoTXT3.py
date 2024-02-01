#Expressão WITH = com ela, o método close é executado automaticamente

texto = 'Cientista de Dados pode ser uma excelente alternativa de carreira.\n'
texto += 'Esses profissionais precisam saber como programar em Python.\n'
texto += 'E, claro, devem ser proficientes em Data Science.'

with open('arquivos/cientista.txt', 'w') as arquivo: #para escrever
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])

with open('arquivos/cientista.txt', 'r') as arquivo: #para ler
    conteudo = arquivo.read()

print(len(conteudo))
print(conteudo)