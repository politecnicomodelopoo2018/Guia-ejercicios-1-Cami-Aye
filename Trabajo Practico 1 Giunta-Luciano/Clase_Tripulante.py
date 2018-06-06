from Clase_Persona import Persona
class Tripulante(Persona):
    def __init__(self):
        self.aviones_habilitados = []

class Servicio(Tripulante):
    def __init__(self):
        self.idiomas = []

class Piloto(Tripulante):
    pass