# Importação de módulos necessários
from abc import ABC, abstractmethod

#Vamos lá, temos que fazer esse código com uma forma mais limpa, colocar as funcões nos códigos auxiliares e só chamar depois.
listanomes = [] #nao sei se precisa estar aqui fora

# Definição da classe abstrata Pessoa
class Pessoa:
    @abstractmethod
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf


class Gerente(Pessoa):
    def __init__(self, nome, cpf, data_nasci, senha):
        super().__init__(nome, cpf)
        self.data_nasci = data_nasci
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nasci}, Senha: {self.senha}"

class Cliente(Pessoa):
    pass