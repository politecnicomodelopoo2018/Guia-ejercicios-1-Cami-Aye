class Mascota(object):
    nombre = None
    saludo = None
    dueno = None

    def Saludar(self, persona):
        if (self.dueno == persona):
            return self.saludo
        return self.saludo.upper()+'!'
    def __init__(self, nombre, dueno):
        self.nombre = nombre
        self.dueno = dueno

class Perro(Mascota):
    saludo = 'guau'

class Gato(Mascota):
    saludo = 'miau'

class Pajarito(Mascota):
    saludo = ""
    def __init__(self, nombre, dueno, saludo = "pio"):
        Mascota.__init__(self, nombre, dueno)
        self.saludo = saludo

    def Saludar(self, persona):
        if self.dueno == persona:
            return self.saludo
        return ""
