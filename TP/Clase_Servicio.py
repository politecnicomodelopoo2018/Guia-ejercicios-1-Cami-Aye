from Clase_Tripulante import Tripulante
from Clase_Persona import Persona
from Clase_Sistema import Sistema
from Clase_avion import Avion

sistema = Sistema()
class Servicio(Persona):

    def __init__(self):
        self.idiomas = []
        # Por que aviones habilitados no se heredan de tripulante
        self.aviones_habilitados = []



    def deserializarservicio(self, persona):

        super().deserializartipo(persona)

        for item in persona["avionesHabilitados"]:
            # Esto es un metodo en sistema llamado Buscar avion pero no me returnea nada aunque entre en el if
            for item2 in sistema.aviones:
                if item == item2.codigo:
                    avionnnn = item
                    self.aviones_habilitados.append(avionnnn)
        for item in persona["idiomas"]:
            self.idiomas.append(item)