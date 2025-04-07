from banco import Banco
from conta import Conta, ContaCorrente, ContaPoupanca
from pessoa import Pessoa, Cliente, Gerente

while True:
    print(f'='*100)
    print('Bem vindo ao Banco em Python!')
    print(f'='*100)
    print('Por favor se identifique:')
    print(f'1)Cliente \t 2)Gerente \t 3)Sair')
    operador = int(input())
    
    if operador == 1:
        print('Olá Cliente, por favor digite seu CPF:')
        cpf = Cliente.acha_cliente()
        

