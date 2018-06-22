from Clase_Persona import Persona
class Pasajero(Persona):
    vip = None
    solicitudes_especiales = None


    def deserializarpasajero(self, persona):
        super().deserializartipo(persona)
        self.vip = persona["vip"]
        if "solicitudesEspeciales" in persona:
            self.solicitudes_especiales = persona["solicitudesEspeciales"]




