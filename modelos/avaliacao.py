class Avaliacao:
    def __init__(self, cliente='', nota=0):
        self._cliente = cliente
        self._nota = nota

    @property
    def nota(self):
        return self._nota
    
    @property
    def cliente(self):
        return self._cliente