from Clase_canciones import Canciones
class Discografica(object):
    nombre = None

    def __init__(self):
        self.albumes = []


    def SetNombre(self, nombre):
        self.nombre = nombre

    def AgregarAlbum(self, album):
        self.albumes.append(album)

# Listado completo de canciones escritas por autores de una nacionalidad ingresada.

    def ListaCancionesPais(self, pais):
        listaCancionesPais = []
        for item in self.albumes:
            for item2 in item.canciones:
                for item3 in item2.autores:
                    if item3.nacionalidad == pais:
                        listaCancionesPais.append(item2)

        return listaCancionesPais
