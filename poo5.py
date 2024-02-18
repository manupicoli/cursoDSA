#Métodos são os comportamentos que você executa nos objetos da classe
#os métodos de classes sempre incluem o parâmetro SELF como primeiro argumento, que se refere ao objeto atual de cada classe.
#MÉTODO INIT: é chamado quando um objeto é criado a partir da classe. É usado para inicializar os atributos do objeto.
class Circulo():
    #o valor de pi é constante, portanto pode ser inicializado fora do método construtor
    pi = 3.14

    #método construtor: quando um objeto dessa classe for criado, esse método será executado
    def __init__(self, raio = 5):
        self.raio = raio

    def area(self):
        #especificamos que a variável pi vem da classe Circulo
        return (self.raio * self.raio) * Circulo.pi
    
    #método para definir um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    #metodo para retornar o valor de raio
    def getRaio(self):
        return self.raio
    
    #nas classes é muito comum ter os métodos SET (para configurar) e GET (para retornar o valor)

#criando um objeto da classe Circulo, uma instância da classe
#nesse momento, o método construtor é executado
circ = Circulo()

print(circ.getRaio())

#sobrescrevendo o valor do raio
cric1 = Circulo(7)

print(cric1.getRaio())

print('A área é igual a: ', circ.area())

#definindo um novo valor de área com o método set
circ.setRaio(3)

print('A área é igual a: ', circ.area())