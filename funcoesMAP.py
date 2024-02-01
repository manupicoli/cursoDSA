#Função MAP
#aplica determinada função a cada um dos elementos de uma estrutura iterável (lista, tupla, etc.)
def potencia(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]

numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado)

def fahrenheit(T):
    return ((float(9)/5) * T+32)

def celsius(T):
    return ((float(5)/9) * T-32)

temperaturas = [0, 22.5, 40, 100]

list(map(fahrenheit, temperaturas)) #coloca o resultado em uma lista

#também podemos utilizar um loop
for temp in map(fahrenheit, temperaturas):
    print(temp)

#utilizando o lambda
print(list(map(lambda x: (5/9) * (x - 32), temperaturas)))

#somando elementos de 2 listas
a = [3,6,9,8]
b = [10,6,3,2]

print(list(map(lambda x,y:x+y, a, b)))