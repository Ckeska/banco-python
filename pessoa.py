#Vamos lá, temos que fazer esse código com uma forma mais limpa, colocar as funcões nos códigos auxiliares e só chamar depois.
listanomes = [] #nao sei se precisa estar aqui fora

class Pessoa:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        pass

class Gerente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
    pass

class Cliente(Pessoa):
    pass