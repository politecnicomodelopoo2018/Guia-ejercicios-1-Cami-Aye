from Clase_Sistema import Sistema
class Vuelo(object):
    avion = None
    fecha = None
    hora = None
    origen = None
    destino = None
    def __init__(self):
        self.tripulantes = []
        self.pasajeros = []

#Deserealizacion:

    def deserializarCodigoAvion(self, vuelo):
        codigo_vuelo = vuelo["avion"]
        sistema = Sistema()
        avion = sistema.BuscarAvion(codigo_vuelo)
        return avion

    def deserializarDniPasajeros(self, vuelo):
        lista_codigo_pasajero = vuelo["pasajeros"]
        lista_pasajeros = []
        sistema = Sistema()
        for codigo_pasajero in lista_codigo_pasajero:
            pasajero = sistema.BuscarPasajero(codigo_pasajero)
            lista_pasajeros.append(pasajero)
        return lista_pasajeros

    def deserializarDniTripulante(self, vuelo):
        lista_codigo_tripulante = vuelo["tripulantes"]
        lista_tripulantes = []
        sistema = Sistema()
        for codigo_tripulante in lista_codigo_tripulante:
            pasajero = sistema.BuscarTripulante(codigo_tripulante)
            lista_tripulantes.append(pasajero)
        return lista_tripulantes

    def AsignarVuelo(self, vuelo):
        sistema = Sistema()
        self.avion = self.deserializarCodigoAvion(vuelo)
        self.tripulantes = self.deserializarDniTripulante(vuelo)
        self.pasajeros = self.deserializarDniPasajeros()
        self.hora = vuelo["hora"]
        self.destino = vuelo["destino"]
        self.origen = vuelo["origen"]
        self.fecha = sistema.StringToDate(vuelo["fecha"])


