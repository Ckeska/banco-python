# Importação de módulos necessários
from abc import ABC, abstractmethod
import datetime as dt
#Vamos lá, temos que fazer esse código com uma forma mais limpa, colocar as funcões nos códigos auxiliares e só chamar depois.

# Definição da classe abstrata Pessoa
class Pessoa:
    @abstractmethod
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
    @abstractmethod
    def acha_cliente(self,cpf=None):
        pass
    
class Cliente(Pessoa):
    def __init__(self, nome, cpf, data_nasci, senha):
        super().__init__(nome, cpf)
        self.data_nasci = data_nasci
        self.senha = senha
        self.lista = []
    # Definição do construtor da classe Cliente
    @classmethod
    def novo_cliente():
        nome = input('Digite o nome do Cliente:')
        cpf = int(input('Digite o cpf do Cliente:'))
        data_nasci = input('Digite a data de nascimento do Cliente:')
        senha = input('Digite a senha do Cliente:')
        return Cliente(nome,cpf,data_nasci,senha)
    
    
    def arruma_cliente():
        nome = input('Digite o nome do Cliente:')
        cpf = int(input('Digite o cpf do Cliente:'))
        data_nasci = input('Digite a data de nascimento do Cliente:')
        senha = input('Digite a senha do Cliente:')
        return Cliente(nome,cpf,data_nasci,senha)
    
    def acha_cliente(self,cpf=None):
        #Chamada de uma função de busca
        if cpf is None:
            cpf = int(input())
        return self.banco.clientes.get(cpf) 
    
    
class Gerente(Pessoa):
    def __init__(self, nome, cpf, data_nasci, senha):
        super().__init__(nome, cpf)
        self.data_nasci = data_nasci
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nasci}, Senha: {self.senha}"
    
    def cria_cliente(self):
        # Chamada de uma função para a crição de cliente
        Cliente.novo_cliente()
        pass
    
    def edita_cliente(self, cliente:Cliente):
        print(cliente)
        print("Há alguma informação incorreta?")
        sn = str(input('Sim ou Não?'))
        if sn == 'Sim':
            print('Por favor escreva a informação que está errada:')
            campo = input()
        Cliente.arruma_cliente(cliente,campo)
     
        
    def acha_cliente(self,cpf=None):
        #Chamada de uma função de busca
        if cpf is None:
            cpf = int(input('Digite o cpf do cliente em questão:'))
        return self.banco.clientes.get(cpf) 
    
    