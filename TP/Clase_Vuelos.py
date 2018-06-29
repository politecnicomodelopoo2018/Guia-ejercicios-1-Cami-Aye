from Clase_Sistema import Sistema
sistema = Sistema()
class Vuelo(object):
    avion = None
    fecha = None
    hora = None
    origen = None
    destino = None
    def __init__(self):
        self.tripulantes = []
        self.pasajeros = []

#Deserializacion:

    def deserializarCodigoAvion(self, vuelo):
        codigo_vuelo = vuelo["avion"]
        avion = sistema.BuscarAvion(codigo_vuelo)
        return avion

    def deserializarDniPasajeros(self, vuelo):
        lista_codigo_pasajero = vuelo["pasajeros"]
        lista_pasajeros = []
        for codigo_pasajero in lista_codigo_pasajero:
            pasajero = sistema.BuscarPasajero(codigo_pasajero)
            lista_pasajeros.append(pasajero)
        return lista_pasajeros

    def deserializarDniTripulante(self, vuelo):
        lista_codigo_tripulante = vuelo["tripulacion"]
        lista_tripulantes = []
        for codigo_tripulante in lista_codigo_tripulante:
            pasajero = sistema.BuscarTripulante(codigo_tripulante)
            lista_tripulantes.append(pasajero)
        return lista_tripulantes

    def AsignarVuelo(self, vuelo):
        self.avion = self.deserializarCodigoAvion(vuelo)
        self.pasajeros = self.deserializarDniPasajeros(vuelo)
        self.tripulantes = self.deserializarDniTripulante(vuelo)
        self.hora = vuelo["hora"]
        self.destino = vuelo["destino"]
        self.origen = vuelo["origen"]
        self.fecha = sistema.StringToDate(vuelo["fecha"])


    #Ejercicio 1
    def NominaPasajeros(self):
        return self.pasajeros

    #Ejercicio 2
    def PasajeroMasJoven(self):
        pasajero_mas_joven = None
        pasajero_joven = None
        contador = 0
        for pasajero in self.pasajeros:
            if contador == 0:
                pasajero_mas_joven = pasajero.fecha_nac
                pasajero_joven = pasajero
            elif contador > 0:
                if pasajero_mas_joven < pasajero.fecha_nac:
                    pasajero_mas_joven = pasajero.fecha_nac
                    pasajero_joven = pasajero
            contador += 1
        return pasajero_joven

    #Ejercicio 6
    def PasajerosVipONecesidad(self):
        ListaPasajeros = []
        for pasajeros in self.pasajeros:
            if pasajeros.vip == 1:
                ListaPasajeros.append(pasajeros)
            else:
                if pasajeros.solicitudes_especiales != None:
                    ListaPasajeros.append(pasajeros)
        return ListaPasajeros

    #Ejercicio 7
    def IdiomasEnCadaVuelo (self):
        lista_idiomas = []
        for tripulacion in self.tripulantes:
            if tripulacion.tipo == "Servicio":
                for idioma in tripulacion.idiomas:
                    if idioma not in lista_idiomas:
                        lista_idiomas.append(idioma)
        return lista_idiomas
