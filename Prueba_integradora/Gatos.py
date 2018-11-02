class Gato(object):
    nombre = None
    saludo = "Miau"
    tipo = "Gato"

    def SetGato(self, nombre):
        self.nombre = nombre

    def ModificarGato(self, nombre_nuevo):
        self.nombre = nombre_nuevo