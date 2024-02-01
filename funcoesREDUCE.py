#Função REDUCE
#movida para o pacote FUNCTOOLS
from functools import reduce

lista = [47, 11, 42, 13]

def soma(a, b):
    x = a + b
    return x

print(reduce(soma, lista)) #aplica a função soma na lista, para reduzir o resultado em um só número

print(reduce(lambda x,y: x+y, lista)) #usando a função lambda

#podemos usar essa função para achar o maior valor da lista

max = lambda a,b: a if (a > b) else b

print(reduce(max, lista))