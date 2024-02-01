#FILTER
#funciona como um filtro para um objeto iterável
#retorna um iterator, por isso, para visualizar os resultados, convertemos para lista

def verificaPAR(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print(list(filter(verificaPAR, lista)))

#usando a função lambda

print(list(filter(lambda x: x%2==0, lista)))

#outra ideia

print(list(filter(lambda x: x < 8, lista)))