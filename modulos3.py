#Manipulando matrizes
#array é melhor para armazenar e analisar os dados
#matriz é melhor para realizar operações matemáticas em si

import numpy

arr9 = numpy.array([[1, 2, 3], [4, 5, 6]]) #lista de listas

print(arr9)

#criando uma matriz 2x3 com apenas números 1

arr10 = numpy.ones((2, 3))

print(arr10)

#criando uma matriz com a função matrix:

lista = [[12, 81, 22], [0, 34, 59], [21, 48, 94]]

arr11 =  numpy.matrix(lista)

print(arr11)

#indexação nas matrizes

print(arr11[2, 1]) #linha de indice 2, coluna de indice 1

print(arr11[0:2, 2]) #elementos na linha entre indice 0 e 2 (sendo o 2 exclusivo), coluna indice 2

#também podemos alterar os elementos da matriz dessa forma
arr11[1, 0] = 100
print(arr11)

#para forçar a alteração do tipo de dado 

arr12 = numpy.array([1, 2], dtype=numpy.float64) #vai armazenar os dados como float
print(arr12.dtype)

#para verificar o tamanho de bytes ocupados

print(arr12.itemsize) #bytes por item
print(arr12.nbytes) #total de bytes
