#Utilizando o pacote OS = operational system
#é um pacote python que permite a interação com o sistema operacional de maneira mais simples, rápida e segura

import os

texto = 'Cientista de Dados pode ser uma excelente alternativa de carreira.\n'
texto += 'Esses profissionais precisam saber como programar em Python.\n'
texto += 'E, claro, devem ser proficientes em Data Science.'

arquivo = open(os.path.join('arquivos/cientista.txt'), 'w') #o arquivo será aberto a partir da função join do os

for palavra in texto.split():
    arquivo.write(palavra + ' ')

arquivo.close()