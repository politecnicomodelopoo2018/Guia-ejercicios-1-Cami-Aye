from Clase_Persona import Persona
class Pasajero(Persona):
    vip = None
    def __init__(self):
        self.solicitudes_especiales = []
