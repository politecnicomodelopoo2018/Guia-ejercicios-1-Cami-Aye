import datetime
class Sistema(object):
    __instancia = None
    def __new__(cls):

        if Sistema.__instancia is None:
            Sistema.__instancia = object.__new__(cls)
        return Sistema.__instancia
    def __init__(self):
        self.personas = []
        self.aviones =  []
        self.vuelos = []
#Buscar
    def BuscarAvion(self, codigo_avion):
        for item in self.aviones:
            if codigo_avion == item.codigo:
                return item
    def BuscarPasajero(self, codigo_pasajero):
        for item in self.personas:
            if item.DNI == codigo_pasajero:
                return item

    def BuscarTripulante(self, codigo_tripulante):
        for item in self.personas:
            if item.DNI == codigo_tripulante:
                return item

    def StringToDate(self, fecha):
        fecha_date = datetime.strptime(fecha, '%dd/%mm/%Y')
        return fecha_date