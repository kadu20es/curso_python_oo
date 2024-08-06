import os

os.system('clear')

'''
from modelos import pessoa

pessoa = pessoa.Pessoa('João', 40, 'Analista de TI')
print(pessoa)

pessoa.aniversario()
print(pessoa)

pessoa.saudacao()
'''
'''
from modelos.conta_bancaria import ContaBancaria

conta1 = ContaBancaria('Joana Prado', 5000)
conta2 = ContaBancaria('Tiazinha', 8000)

print(conta1) # não
print(conta2) # não

conta2._saldo = 5000

print(conta2)
'''

'''
print(conta1) # não
print(conta2) # não
ContaBancaria.ativar_conta(conta2)
print(conta1) # não
print(conta2) # sim
ContaBancaria.ativar_conta(conta1)
ContaBancaria.ativar_conta(conta2)
print(conta1) # sim
print(conta2) # não
'''
'''
from modelos.restaurante import Restaurante

restaurante1 = Restaurante('Bistrô', 'Gourmet')
restaurante2 = Restaurante('Pizza Express', 'Fast Food')
restaurante3 = Restaurante('Japa San', 'Oriental')

restaurante3.alternar_estado()

restaurante3.receber_avaliacao('Gui', 8)
restaurante3.receber_avaliacao('Lara', 9)
restaurante3.receber_avaliacao('Bite', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()

    '''

from modelos.livro import Livro

livro0 = Livro('João e o pé de feijão', 'João', 1980)
livro1 = Livro('João e o pé de feijão2 - o retorno', 'João', 1980)
livro2 = Livro('Pedro e a estação', 'Pedro', 1980)
livro3 = Livro('Meu pé de laranja lima', 'Monteiro Lobato', 1908)
livro4 = Livro('Entrevista com o vampiro', 'Anne Rice', 1980)
livro5 = Livro('Eu e minha boca grande', 'Tiago Pereira', 1983)
livro6 = Livro('A casa da mãe Joana', 'Pereirão', 1984)



print('----------------')
livro3.verificar_disponibilidade(1980)

#print(livro1.verificar_disponibilidade(1980))
livro1.emprestar_livro()

Livro.verificar_disponibilidade(1980)
#print(livro1.verificar_disponibilidade(1980))