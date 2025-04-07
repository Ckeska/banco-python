from abc import ABC, abstractmethod

class Conta:
    def __init__(self,conta,saldo):
        self.conta = conta
        self.saldo = saldo
        
    @abstractmethod
    def saque(self,valor):
        pass
    
    def deposito(self, valor):
        self.saldo += valor
    
        
class ContaCorrente(Conta):
    def __init__(self, conta, saldo,limite=500):
        super().__init__(conta, saldo)
        self.limite = limite
    def saque(self,valor):
        if valor > (self.saldo + self.limite):
            print('Não há como sacar esse valor.')
        else:
            self.saldo -= valor
        

class ContaPoupanca(Conta):
    def __init__(self, conta, saldo):
            super().__init__(conta, saldo)
    def saque(self,valor):
        if valor > self.saldo:
            print('Não há como sacar esse valor.')
        else:
            self.saldo -= valor
    
class GerenciadeConta:
    
    pass
