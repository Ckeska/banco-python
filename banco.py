class Banco():
    def __init__(self):
        self.agencias = [111,222,333]
        self.contas = []
        self.clientes = []
        pass
    
    def inserir_conta(self,conta):
        self.contas.append(conta)
        pass
    
    def verificar_conta(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False
        return True
    