class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    def ativo(self):
        return self._ativo
    
    
    def __str__(self):
        return f"""------------------------------------
        Titular: {self.titular}
        Saldo: {self.saldo}
        Conta Ativa: {'sim' if self._ativo else 'não'}"""
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = not conta._ativo
    