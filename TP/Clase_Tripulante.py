from Clase_Sistema import *
from Clase_Persona import *

sistema = Sistema()

class Tripulante(Persona):
    def __init__(self):

        self.aviones_habilitados = []

    def deserializarTripulante(self, persona):
        super().deserializartipo(persona)
        for item in persona["avionesHabilitados"]:
            avion = sistema.BuscarAvion(item)
            self.aviones_habilitados.append(avion)




class Servicio(Tripulante):
    def __init__(self):
        self.idiomas = []

    def deserializarservicio(self, persona):
        Tripulante().deserializarTripulante(persona)
        for item in persona["idiomas"]:
            self.idiomas.append(item)


class Piloto(Tripulante):
    pass
