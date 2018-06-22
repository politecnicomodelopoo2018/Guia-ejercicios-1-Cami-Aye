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




class Piloto(Tripulante):
    pass