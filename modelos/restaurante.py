from modelos.avaliacao import Avaliacao

# cria uma classe
class Restaurante:
    restaurantes = []

    # construtor de classe
    def __init__(self, nome, categoria): 
        self.nome = nome.title() # title converte a primeira letra para maiúscula
        self.categoria = categoria
        self._ativo = False # torna a propriedade protegida
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    # método especial do python - imprime os dados do retorno apenas chamando o nome da variável de instância
    def __str__(self):
        return f'Restaurante: {self.nome} | Categoria: {self.categoria} | Status: {'ativo' if self._ativo else 'inativo'} | Nota: {self.media_avaliacao}'
    
    # método de classe
    @classmethod
    def listar_restaurantes(cls):
        print('+---------------------------+---------------------------+---------------------------+------------------------+')
        print(f'| {'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status (ativo/inativo)'.ljust(25)} | {'Avaliação'.ljust(22)} |')
        print('----------------------------+---------------------------+---------------------------+------------------------+')
        for restaurante in Restaurante.restaurantes:
            print(f'| {restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {str(restaurante.media_avaliacao).ljust(22)} |')
        print('+---------------------------+---------------------------+---------------------------+------------------------+')
    
    @property
    def ativo(self):
        return '☑'if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo # nega

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media