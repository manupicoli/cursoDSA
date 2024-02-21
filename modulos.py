#ciência de dados se resume em operações com matrizes
#Os arrays NumPy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidades de dados,
#Além disso, o NumPy permite a fácil leitura e escrita de arquivos de dados, 
#integração com outras bibliotecas Python e suporte a operações em paralelo usando várias CPUs ou GPUs.
#uma das grandes vantagens do array numpy é a indexação, ou seja,
#você pode fatiar um array numpy de várias formas

import numpy

arr = numpy.array([10, 21, 32, 43, 48, 15, 76, 57, 89])

print(arr)

#indexação em arrays numpy

indices = [1, 5, 7, 8]

print(arr[indices]) #vai retorar os valores correspondentes aos indices da lista

#criar uma máscara booleana para números pares

mask = (arr % 2 == 0) #vai retornar True ou False

print(mask)
print(arr[mask]) #retorna os valores True

#para alternar o valor de um indice

arr[0] = 100
print(arr)

#não é permitido mais de um tipo de dado dentro de um mesmo array

try:
    arr[0] = 'Novo elemento'
except:
    print('Operação não permitida!')