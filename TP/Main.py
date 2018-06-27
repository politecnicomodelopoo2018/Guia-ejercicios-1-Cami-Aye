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
'''
for item in sistema.aviones:
    print("avion: ", item.codigo, " cantidad maxima de pasajeros: ", item.cantidad_pasajeros_maximo, " cantidad necesaria de tripulantes: ", item.cantidad_tripulantes_necesaria)
'''


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
'''
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
'''


# Vuelos json

for item in d["Vuelos"]:
    vuelito = Vuelo()
    vuelito.AsignarVuelo(item)
    sistema.AgregarVuelo(vuelito)
'''
for item in sistema.vuelos:
    print("avion: ", item.avion.codigo, " fecha: ", item.fecha, " hora: ", item.hora, " origen: ", item.origen, " destino: ", item.destino)
    print(" tripulantes: ")
    for item2 in item.tripulantes:
        print(item2.DNI)
    print(" pasajeros: ")
    for item2 in item.pasajeros:
        print(item2.DNI)
'''
archivo.close()


#Ejercicio 1

'''
destiny = input("Ingrese destino del vuelo: ")
vuelo = sistema.BuscarVuelo(destiny)
if vuelo != None:
    nomina = vuelo.NominaPasajeros()
    print(nomina)
else:
    print("El vuelo no existe")

'''

#Ejercicio 2

'''
destiny = input("Ingrese destino del vuelo: ")
vuelo = sistema.BuscarVuelo(destiny)
if vuelo != None:
    Pasajero_joven = vuelo.PasajeroMasJoven()
    print(Pasajero_joven, Pasajero_joven.nombre)
else:
    print("El vuelo no existe")
'''

#Ejercicio 3
'''
Lista_vuelos = sistema.TripulacionMinimaNoAlcanzada()
for item in Lista_vuelos:
    print(item.destino)'''

#Ejercicio 4

Lista_vuelos = sistema.VuelosTripuladosSinAutorizacion()
for item in Lista_vuelos:
    print(item.destino)


#Ejercicio 5
'''
tripulante = input("Ingrese tripulante: ")
confirmacion = sistema.Verificar_Vuelos_Por_Fecha(tripulante)
if confirmacion == True:
    print("Viajo mas de una vez un mismo dia")
else:
    print("No viajo mas de una vez un mismo dia")
'''

#Ejercicio 6
'''
destiny = input("Ingrese destino del vuelo: ")
vuelo = sistema.BuscarVuelo(destiny)
lista_pasajerosConNecesidadesOVp = []
if vuelo != None:
    lista_pasajerosConNecesidadesOVp = vuelo.PasajerosVipONecesidad()
else:
    print("El vuelo no existe")
for item in lista_pasajerosConNecesidadesOVp:
     print(item.nombre)
'''

#Ejercicio 7
'''
destiny = input("Ingrese destino del vuelo: ")
vuelo = sistema.BuscarVuelo(destiny)
lista_idiomas = []
if vuelo != None:
    lista_idiomas = vuelo.IdiomasEnCadaVuelo()
    print(lista_idiomas)
else:
    print("El vuelo no existe")
'''