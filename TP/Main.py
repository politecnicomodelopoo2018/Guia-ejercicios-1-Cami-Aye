import json
from Clase_avion import Avion
from Clase_Sistema import Sistema
from Clase_Tripulante import *
from Clase_Pasajero import Pasajero
from Clase_Vuelos import Vuelo
from Clase_Servicio import Servicio

archivo = open("datos.json", "r")
d = json.loads(archivo.read())

sistema = Sistema()
# Aviones json

for item in d["Aviones"]:
    avioncito = Avion()
    avioncito.AsignarAvion(item)
    sistema.AgregarAvion(avioncito)

for item in sistema.aviones:
    print("avion: ", item.codigo, " cantidad maxima de pasajeros: ", item.cantidad_pasajeros_maximo, " cantidad necesaria de tripulantes: ", item.cantidad_tripulantes_necesaria)



# Personas json


for item in d["Personas"]:
    if item["tipo"] == "Pasajero":
        personita = Pasajero()
        personita.deserializarpasajero(item)
        sistema.AgregarPersona(personita)

    elif item["tipo"] == "Piloto":
        personita = Piloto()
        personita.deserializarTripulante(item)
        sistema.AgregarPersona(personita)
    elif item["tipo"] == "Servicio":
        personita = Servicio()
        personita.deserializarservicio(item)
        sistema.AgregarPersona(personita)

for item in sistema.personas:
    if item.tipo == 'Pasajero':
            print("Nombre: ", item.nombre, "Apellido: ", item.apellido, "Fecha de nacimiento: ", item.fecha_nac, "DNI: ", item.DNI, "VIP: ", item.vip, "Solicitudes Especiales: ", item.solicitudes_especiales)

    elif item.tipo == 'Piloto':
            print("Nombre: ", item.nombre, "Apellido: ", item.apellido, "Fecha de nacimiento: ", item.fecha_nac, "DNI: ", item.DNI)
            print("Aviones Habilitados: ")
            for avion_habilitado in item.aviones_habilitados:
                print(avion_habilitado.codigo)
    elif item.tipo == 'Servicio':
            print("Nombre: ", item.nombre, "Apellido: ", item.apellido, "Fecha de nacimiento: ", item.fecha_nac, "DNI: ", item.DNI)
            print("Aviones Habilitados: ")
            for avion_habilitado in item.aviones_habilitados:
                print(avion_habilitado)
            for idioma in item.idiomas:
                print(idioma)



# Vuelos json

for item in d["Vuelos"]:
    vuelito = Vuelo()
    vuelito.AsignarVuelo(item)
    sistema.AgregarVuelo(vuelito)

for item in sistema.vuelos:
    print("avion: ", item.avion.codigo, " fecha: ", item.fecha, " hora: ", item.hora, " origen: ", item.origen, " destino: ", item.destino)
    print(" tripulantes: ")
    for item2 in item.tripulantes:
        print(item2.DNI)
    print(" pasajeros: ")
    for item2 in item.pasajeros:
        print(item2.DNI)




archivo.close()