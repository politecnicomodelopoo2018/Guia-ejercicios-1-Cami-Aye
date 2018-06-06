class Avion(object):
    codigo = None
    cantidad_pasajeros_maximo = None
    cantidad_tripulantes_necesaria = None

#Deserealizacion

    def AsignarAvion(self, avion):
        self.codigo = avion["codigoUnico"]
        self.cantidad_pasajeros_maximo = avion["cantidadDePasajerosMaxima"]
        self.cantidad_tripulantes_necesaria = avion["cantidadDeTripulaciónNecesaria"]


