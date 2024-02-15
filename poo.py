#Em POO, o foco está na criação de objetos que interagem entre si para realizar tarefas

#a classe vai representar um objeto, que pode ser manipulado através de atributos e métodos
class Livro():
    #funções dentro da classe = métodos
    def __init__(self): #metodo construtor
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 9988888
        print('Construtor chamado para criar um objeto dessa classe')
    
    def imprime(self):
        print(f'Foi criado o livro {self.titulo} com o ISBN {self.isbn}')


Livro1 = Livro()

#atributo:
print(Livro1.titulo)

#método:
print(Livro1.imprime())