
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
        print('Bem vindo de volta {}!'.format(Pessoa.nome))
        print('Qual conta você deseja acessar?')
        opconta = int(input(f'1)Conta Corrente \t 2)Conta Poupança \t 3)Sair'))
        
        if opconta== 1:
            Cliente.verificar_senha_segura()
            if Cliente.verificar_senha_segura() == True:
                print('O que deseja fazer hoje?')
                opcc = int(input(f'1)Ver saldo \t 2)Fazer Depósito \t 3) Fazer Saque'))
                if opcc == 1:
                    print(f'Seu saldo é de R${Conta.saldo:.2f}')
                    break
                
                if opcc == 2:
                    ContaCorrente.deposito()
                    break
                    
                if opcc == 3:
                    ContaCorrente.saque()
                    break
            else:
                break 
        if opconta == 2:
            Cliente.verificar_senha_segura()
            if Cliente.verificar_senha_segura() == True:
                print('O que deseja fazer hoje?')
                opcp = int(input(f'1)Ver saldo \t 2)Fazer Depósito \t 3) Fazer Saque'))
                if opcp == 1:
                    print(f'Seu saldo é de R${Conta.saldo:.2f}')
                    break
                
                if opcp == 2:
                    ContaPoupanca.deposito()
                    break
                    
                if opcp == 3:
                    ContaPoupanca.saque()
                    break
            else:
                break
        if opconta == 3:
            break
        
    if operador == 2:
        print('Olá Gerente, por favor digite seu CPF')
        cpf = int(input())
        if cpf == Gerente(cpf):
            print('Bem vindo de volta {}!'.format(Gerente.nome))
            Gerente.verificar_senha_segura()
            if Gerente.verificar_senha_segura() == True:
                print('O que voce deseja fazer hoje, Gerente?')
                opgerente = int(input(f'1)Adicionar Cliente \t 2)Editar Cliente \t 3)Sair'))
                if opgerente == 1:
                    Gerente.cria_cliente()
                    break
                if opgerente == 2:
                    Gerente.edita_cliente()
                    break
                if opgerente == 3:
                    break
                    
        else:
            print('Seu CPF não corresponde ao CPF do Gerente.')
            break
    if operador == 3:
        break
        
            
        
