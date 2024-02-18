    #ao invés de criar uma classe de maneira estática, usamos parâmetros para permitir que,
#ao criar a instância da classe, seja enviado o título e o código (nesse caso)

class Livro():
    def __init__(self, titulo, isbn): #metodo construtor
        self.titulo = titulo
        self.isbn = isbn
        print('Construtor chamado para criar um objeto dessa classe')
    
    def imprime(self, titulo, isbn):
        print(f'Foi criado o livro {titulo} com o ISBN {isbn}')

Livro2 = Livro('O Poder do Hábito', 77886611)

Livro2.imprime('O Poder do Hábito', 77886611)