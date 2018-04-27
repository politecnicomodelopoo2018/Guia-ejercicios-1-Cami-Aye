class Canciones(object):
    titulo = None


    def __init__(self):
        self.artistas = []
        self.autores = []

    def AgregarArtistas(self, artista):
        self.artistas.append(artista)

    def AgregarAutores(self, autor):
        self.autores.append(autor)
    