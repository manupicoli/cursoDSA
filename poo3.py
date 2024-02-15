class Algoritmo():
    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print('Construtor chamado para criar um objeto dessa classe')

algo1 = Algoritmo(tipo_algo='Random Forest')

algo2 = Algoritmo(tipo_algo='Deep Learning')

print(algo1.tipo)

print(algo2.tipo)