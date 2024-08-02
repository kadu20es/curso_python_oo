class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"""
            Nome: {self.nome}\n
            Idade: {self.idade}\n
            Profissao: {self.profissao}\n 
        """
    
    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        if not self.profissao:
            print(f'Olá, {self.nome}')
            return
        
        print(f'Olá, {self.nome}. Feliz dia do {self.profissao}')
        
        

