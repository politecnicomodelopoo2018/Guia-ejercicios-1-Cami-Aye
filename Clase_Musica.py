from Clase_Programas import Programa
class CategoriaMusica(Programa):
    musicalizador = None
    def __init__(self):

        self.estilosMusica = []

    def SetMusicalizador(self, persona):
        self.musicalizador = persona
    def AgregarEstiloMusica(self, estilo):
        for item in self.estilosMusica:
            if item == estilo:
                return False
        self.estilosMusica.append(estilo)
