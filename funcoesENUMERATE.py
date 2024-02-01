#ENUMERATE
#retorna um objeto enumerado, um índice de cada elemento dentro de um objeto iterável

seq = ['a', 'b', 'c']

print(list(enumerate(seq)))

for indice, valor in enumerate(seq):
    print(indice, valor)

for indice, valor in enumerate(seq):
    if indice >= 2: #usando os indices para aplicar filtros
        break
    else:
        print(valor)

lista = ['Marketing', 'Tecnologia', 'Business']

for i, item in enumerate(lista):
    print(i, item)

for i, item in enumerate('Data Science Academy'):
    print(i, item)

for i, item in enumerate(range(10)):
    print(i, item)