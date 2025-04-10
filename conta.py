from abc import ABC, abstractmethod
from banco import agencias as agencia

#Implentação de uma classe abstrata
class Conta(ABC):
    def __init__(self,agencia,conta,saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abstractmethod
    def saque(self,valor):
        pass
    
    @abstractmethod
    def deposito(self, valor):
        pass
    
        
class ContaCorrente(Conta):
    def __init__(self,conta, saldo,limite=500):
# Aqui falta um argumento (acho que é agencia)
        super().__init__(agencia,conta, saldo)
        self.limite = limite
    
    def saque(self,valor):
        if valor > (self.saldo + self.limite):
            print('Não há como sacar esse valor.')
        else:
            self.saldo -= valor
            print('O valor foi sacado com sucesso! ')
    
    def deposito(self):
        return print('Não é possível fazer essa operação nessa conta.')
        

class ContaPoupanca(Conta):
    def __init__(self, conta, saldo):
# squi também falta a agência
            super().__init__(agencia,conta, saldo)
    
    def saque(self,valor):
        if valor > self.saldo:
            print('Não há como sacar esse valor.')
        else:
            self.saldo -= valor
            print('O valor foi sacado com sucesso!')
    
    def deposito(self, valor):
        valor = int(input('Digite o valor que será depositado.'))
        if valor <= 0:
            print('Não é possivel realizar o depósito com esse valor.')
        else:
            self.saldo += valor 
            print('O valor foi depositado com sucesso!')