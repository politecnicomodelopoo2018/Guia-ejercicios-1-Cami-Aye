class Dueno(object):
    nombre = None
    def __init__(self):
        self.mascotas = []

    def AgregarMascota(self, nombre):
        self.mascotas.append(nombre)

    def BorrarMascota(self, nombre):
        self.mascotas.remove(nombre)