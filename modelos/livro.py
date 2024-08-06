class Livro:
    livros = []

    def __init__(self, titulo = '', autor = '', ano_publicacao = 0):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)


    def __str__(self):
        return f'Titulo: {self._titulo} | Autor: {self._autor} | Ano de publicacao: {self._ano_publicacao} | Status: {'disponível' if self._disponivel else 'não disponível'} '
    
    def emprestar_livro(self):
        if self._disponivel:
            self._disponivel = False
        return

    @classmethod
    def verificar_disponibilidade(self, ano):
        '''
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
        '''
        print('+-----------------------------------------------+---------------------------+---------------------------+------------------------+')
        print(f'| {'Título'.ljust(45)} | {'Autor'.ljust(25)} | {'Ano de lançamento'.ljust(25)} | {'Status (ativo/inativo)'.ljust(22)} |')
        print('+-----------------------------------------------+---------------------------+---------------------------+------------------------+')
        
        for livro in Livro.livros:  
            if livro._disponivel and livro._ano_publicacao == ano:
                print(f'| {livro._titulo.ljust(45)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(25)} | {'Disponível'.ljust(22) if livro._disponivel else 'Indisponível'.ljust(22)} |')
                print('+-----------------------------------------------+---------------------------+---------------------------+------------------------+')
                #livros_disponiveis.append(livro)
            
        
        print("Não há livros disponíveis neste ano.")
