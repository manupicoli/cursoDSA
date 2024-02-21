#Funções NumPy

import numpy

arr2 = numpy.array([1, 2, 3, 4, 5])

#função arange = equivale a função range em python, mas cria um array NumPy

arr3 = numpy.arange(0, 50, 5)

print(arr3)

#array preechido com zeros

arr4 = numpy.zeros(10)

print(arr4)

#matriz com a diagonal preenchida com 0

arr5 = numpy.eye(3)

print(arr5)

#criar uma matriz onde os valores passados como parametro formarão a diagonal principal

arr6 = numpy.diag(numpy.array([1, 2, 3, 4]))

print(arr6)

#função linspace e logspace
#linspace = inicializar uma lista de elementos com uma sequência de números igualmente espaçados dentro do intervalo especificado

print(numpy.linspace(0, 10))

#logspace = valores igualmente espaçados em escala logarítmica dentro do intervalo especificado

print(numpy.logspace(0, 10))