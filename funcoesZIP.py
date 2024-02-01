#ZIP
#agrupa elementos de estruturas iteráveis em pares
#retorna um objeto zip quw pode ser convertido

x = [1, 2, 3]
y = [4, 5, 6]

print(list(zip(x, y)))

print(list(zip('ABCD', 'xy'))) #quando tem quantidades diferentes
#forma os pares até onde for possível, o que "sobra" é descartado

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 4, 'd': 5}

print(list(zip(dict1, dict2))) #por padrão, a função zip une as chaves dos dicionários
#também podem ser utilizados os calores
print(list(zip(dict1.values(), dict2.values())))

#possibilidade de trocar chaves e valores entre dois dicionários

def trocaValores(dict1, dict2):
    dictTemp = {}

    for dict1key, dict2value in zip(dict1, dict2.values()):
        dictTemp[dict1key] = dict2value

    return dictTemp

print(trocaValores(dict1, dict2))