class Equipo(object):
    nombre = None
    barrio = None
    capitan = None
    def __init__(self):

        DisponibilidadHoraria = []
        Jugadores = []

    def NombrarEquipo (self, nombre):
        self.nombre = nombre

    def SetBarrio (self, barrio):
        self.barrio = barrio

    def ElegirCapitan (self, jugador):
        self.capitan = jugador

    def AgregarJugadores (self, jugador):
        self.Jugadores.append = jugador

    def DecidirHorario (self)
