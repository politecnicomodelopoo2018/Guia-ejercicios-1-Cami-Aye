from datetime import datetime
class Sistema(object):
    __instancia = None
    def __new__(cls):

        if Sistema.__instancia is None:
            Sistema.__instancia = object.__new__(cls)
        return Sistema.__instancia
    def __init__(self):
        self.personas = []
        self.aviones = []
        self.vuelos = []
    #Buscar

    def BuscarAvion(self, codigo_avion):
        for item in self.aviones:
            if codigo_avion == item.codigo:
                allgo = item

                return allgo
    def BuscarPasajero(self, codigo_pasajero):
        for item in self.personas:
            if item.DNI == codigo_pasajero:
                return item


    def BuscarTripulante(self, codigo_tripulante):
        for item in self.personas:
            if item.DNI == codigo_tripulante:
                return item

    def BuscarVuelo(self, destino):
        for item in self.vuelos:
            if item.destino == destino:
                return item

    def StringToDate(self, fecha):
        fecha_date = datetime.strptime(fecha, '%Y-%m-%d')
        return fecha_date

    #Agregar en lista

    def AgregarPersona(self, persona):
        self.personas.append(persona)

    def AgregarVuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def AgregarAvion(self, avion):
        self.aviones.append(avion)

    #Ejercicio 5

    def Fechas_Por_Tripulante(self, tripulante):
        lista_fechas = []
        for item in self.vuelos:
            for item2 in item.tripulantes:
                if tripulante == item2.DNI:
                    print(item.fecha)
                    lista_fechas.append(item.fecha)
        print(lista_fechas)
        return lista_fechas


    def Verificar_Vuelos_Por_Fecha(self, tripulante):
        lista_fechas = self.Fechas_Por_Tripulante(tripulante)
        fecha_anterior = None
        dias = None
        for item in lista_fechas:
            dias = 0
            for item2 in lista_fechas:
                if item == item2:
                    dias += 1
                    if dias > 1:
                        return True
        return False

# Ejercicio 3
    def TripulacionMinimaNoAlcanzada(self):
        ListaVuelosTripulacionNoAlcanzada = []
        for vuelos in self.vuelos:
            contador = len(vuelos.tripulantes)
            if contador < vuelos.avion.cantidad_tripulantes_necesaria:
                ListaVuelosTripulacionNoAlcanzada.append(vuelos)
        return ListaVuelosTripulacionNoAlcanzada

    #Ejercicio 4
    def VuelosTripuladosSinAutorizacion(self):
        Lista_vuelosNoHabilitados = []
        for vuelo in self.vuelos:
            for tripulacion in vuelo.tripulantes:
                if vuelo.avion not in tripulacion.aviones_habilitados:
                    if vuelo not in Lista_vuelosNoHabilitados:
                        Lista_vuelosNoHabilitados.append(vuelo)
        return Lista_vuelosNoHabilitados



