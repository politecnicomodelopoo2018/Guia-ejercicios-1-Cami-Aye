class Discografica(object):
    nombre = None

    def __init__(self):
        self.albumes = []


    def SetNombre(self, nombre):
        self.nombre = nombre

    def AgregarAlbum(self, album):
        self.albumes.append(album)

    def ListaCancionesPais(self, pais):
        listaCancionesPais = []
        for item in self.albumes:
            for item2 in item.canciones:
                if item2.nacionalidad == pais:
                    listaCancionesPais.append(item2)

        return listaCancionesPais


