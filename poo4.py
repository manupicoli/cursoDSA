class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def listFunc(self):
        print('Funcionário(a) ' + self.nome + ' tem salário de R$' + str(self.salario) + ' e o cargo é ' + self.cargo)

Func1 = Funcionario('Mary', 20000, 'Cientista de Dados')

Func1.listFunc()

#USANDO ATRIBUTOS

hasattr(Func1, 'nome') #hasattr = tem atributo, retorna true ou false

setattr(Func1, 'salario', 4500) #faz a mudança de um atributo

getattr(Func1, 'salario') #retorna o valor do atributo

delattr(Func1, 'salario') #deleta um atributo

print(hasattr(Func1, 'salario'))