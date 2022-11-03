class Pessoas:
    def __init__(self, nome, emprego, idade):
        self.nome = nome
        self.emprego = emprego
        self.idade = idade
    def ola(self):
        print(f'Olá, meu nome é {self.nome} tenho {self.idade} anos e sou {self.emprego}')

lucas = Pessoas('Lucas', 'Advogado', 20)
lucas.ola()

print(lucas.__dict__)