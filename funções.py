import math

def NumPrim(num):
    if num % 2 == 0 and num > 2:
        return 'Esse número não é primo'
    for i in range (3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return 'Esse número não é primo'      
    return 'Esse número é primo'

#é possível criar funções utilizando funções built-in do Python e funções de pacotes também

NumPrim(541)

def lowercse(text):
    return text.lower()

#Permite criar módulos em Python (principalmente Programação Orientada a Objetos, criando hierarquia)

def split_string_palavras(texto):
    return texto.split(" ")

#essa função vai separar a string toda vez que encontrar um caracter de espaço. 
#Esse processo é muito utilizado em processamento de linguagem natural, por exemplo.
#Os resultados dessa separação (palavras) são chamados de tokens (menores estruturad possíveis)

#Expressão Lambda = amplamente utilizada em análise e ciência de dados. Cria uma função em tempo de execução, função anônima.
#Normalmente não se atribui a expressão lambda a uma variável, ela é usada no momento em que precisa ser executada.

#LIST COMPREHENSION: um loop dentro de uma lista

[x for x in range(10)]

#Lê-se - Retorne x para cada elemento x na lista de 10 elementos

lista_numeros = [x for x in range(10) if x < 5]

#Nesse caso, estipulamos uma condição!

print(lista_numeros)

lista_frutas = ['banana', 'melancia', 'abacate', 'cereja', 'manga']

nova_lista = []

for x in lista_frutas:
    if 'm' in x:
        nova_lista.append(x)
        
print(nova_lista)

#Utilizando list comprehension:

nova_lista = [x for x in lista_frutas if 'm' in x]

print(nova_lista)

#DICT COMPREHENSION: mesma ideia utilizando dicionários

dict_alunos = {'Bob': 68, 'Michel': 84, 'Zico': 57, 'Ana': 93}

dict_alunos_status = {k:v for k, v in dict_alunos.items()}
print(dict_alunos_status)

dict_alunos = {'Bob': 68, 'Michel': 84, 'Zico': 57, 'Ana': 93}

dict_alunos_status = {k: ('Aprovado' if v > 70 else 'Reprovado') for k, v in dict_alunos.items()}
print(dict_alunos_status)