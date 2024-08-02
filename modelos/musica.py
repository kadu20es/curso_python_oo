class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'Título: {self.titulo} | Artista: {self.artista} | Duração: {self.duracao}'

musica1 = Musica('Baby one more time', 'Britney Spears', 3.32)
musica2 = Musica('Faroeste Caboclo', 'Legião Urbana', 14.22)

print(musica1)
