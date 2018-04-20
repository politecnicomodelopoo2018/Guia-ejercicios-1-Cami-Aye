from Clase_artistas import Artista

class Autores (Artista):

    nacionalidad = None

    def SetNombre(self, nombre):
        self.nombre = nombre


    def SetApellido(self, apellido):
        self.apellido = apellido


    def SetNacimiento(self,fechanac):
        self.Fecha_Nac = fechanac

    def SetNacionalidad(self, pais):
        self.nacionalidad = pais