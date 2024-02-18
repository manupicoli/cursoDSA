#HERANÇA DAS CLASSES
#uma classe filha que herda alguma coisa de uma classe mãe
#permite reduzir a quantidade de código, modularizar melhor o programa, etc.
#herda os atributos e métodos gerais da classe mãe, adicionando novos atributos e métodos específicos
#ou ate mesmo substituí-los e estendê-los conforme necessário

#Criando a classe mãe (superclasse)
#colocamos aqui tudo que é geral para qualquer animal (comer, emitir som)
class Animal():
    def __init__(self):
        print('Animal criado')

    def imprimir(self):
        print('Este é um animal')

    def comer(self):
        print('Hora de comer')
    
    def emitir_som(self):
        #mesma ideia de criar uma lista vazia
        pass #por enquanto não faz nada, mas já definimos o método para que ele possa ser especificado no futuro


class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self) #ao executar o construtor da subclasse, é necessário executar o construtor da classe mãe também
        print('Objeto Cachorro criado')

    #o som Au au é específico do cachorro, por isso vai apenas nessa subclasse
    #podemos sobrescrever o nome de um método
    def emitir_som(self):
        print('Au au!')

class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Objeto Gato criado')

    #o som Miau é específico do cachorro, por isso vai apenas nessa subclasse
    def emitir_som(self):
        print('Miau!')

#características gerais = classe mãe
#características específicas = classe filha
        
rex = Cachorro()

mingau = Gato()

rex.emitir_som()

mingau.emitir_som()

rex.imprimir()

mingau.comer()