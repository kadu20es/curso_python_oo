# cria uma classe

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Restaurante Praça'
restaurante_praca.categoria = 'Gourmet'
restaurante_praca.ativo = False

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizzaria Tarantella'
restaurante_pizza.categoria = 'Pizzaria'
restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]

# vars() exibe os atributos da classe
print(vars(restaurante_pizza))

categoria = restaurante_praca.categoria
restaurante_praca.nome = 'Bistrô'

restaurante_pizza2 = Restaurante()
restaurante_pizza2.nome = "Pizza Place"
restaurante_pizza2.categoria = 'Fast Food'

print('fast food') if restaurante_pizza2.categoria == 'Fast Food' else print('não fast food')


# cria uma classe
import os
os.system('clear')

class Restaurante:
    restaurantes = []

    # construtor de classe
    def __init__(self, nome, categoria): 
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    # método especial do python
    def __str__(self):
        return f"Restaurante: {self.nome} | Categoria: {self.categoria} | Status: {'ativo' if self.ativo else 'inativo'}"
    
    # método de classe
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
    
    

restaurante_praca = Restaurante('Bistro', 'Fast Food')
restaurante_pizza = Restaurante('Pizzaria Tarantella', 'Restaurante')
restaurante_praca.ativo = True

print(restaurante_praca)
print(restaurante_pizza)
print('------------------------------------------')

Restaurante.listar_restaurantes()