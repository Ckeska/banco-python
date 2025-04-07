from abc import ABC, abstractmethod

#Implentação de uma classe abstrata
class Conta(ABC):
    def __init__(self,conta,saldo):
        self.conta = conta
        self.saldo = saldo
        
    @abstractmethod
    def saque(self,valor):
        pass
    
    @abstractmethod
    def deposito(self, valor):
        pass
    
        
class ContaCorrente(Conta):
    def __init__(self, conta, saldo,limite=500):
        super().__init__(conta, saldo)
        self.limite = limite
    def saque(self,valor):
        if valor > (self.saldo + self.limite):
            print('Não há como sacar esse valor.')
        else:
            self.saldo -= valor
    def deposito(self, valor):
        return print('Não é possível fazer essa operação nessa conta.')
        

class ContaPoupanca(Conta):
    def __init__(self, conta, saldo):
            super().__init__(conta, saldo)
    def saque(self,valor):
        if valor > self.saldo:
            print('Não há como sacar esse valor.')
        else:
            self.saldo -= valor
    def deposito(self, valor):
        return super().deposito(valor)     
    
    
class GerenciadeConta:
    
    pass
