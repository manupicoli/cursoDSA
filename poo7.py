#POLIMORFISMO - objetos de diferentes classes (tanto super quanto sub) podem ser tratados de maneira uniforme
#criar um único método que pode ser usado em diferentes objetos com comportamentos diferentes

class Veiculo():
    #usaremos o método construtor apenas na super classe
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self):
        pass

    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print('O carro está acelerando!')

    def frear(self):
        print('O carro está freando!')

class Moto(Veiculo):
    def acelerar(self):
        print('A moto está acelerando!')

    def frear(self):
        print('A moto está freando!')

class Aviao(Veiculo):
    def acelerar(self):
        print('O avião está acelerando!')

    def frear(self):
        print('O avião está freando!')

    def decolar(self):
        print('O avião está decolando!')

#é possível criar uma lista de objetos:
lista_veiculos = [Carro('Porsche', '911 Turbo'), Moto('Honda', 'CB 100R Black Edition'), Aviao('Boeing', '757')]

for item in lista_veiculos:
    item.acelerar()
    item.frear()
    if isinstance(item, Aviao): #verifica se o item em questão é do tipo Aviao
        item.decolar()
    
    print('------')