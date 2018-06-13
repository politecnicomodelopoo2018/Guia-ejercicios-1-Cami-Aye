



import json
from Clase_avion import Avion
from Clase_Sistema import Sistema
from Clase_Tripulante import Piloto
from Clase_Tripulante import Servicio
from Clase_Pasajero import Pasajero

archivo = open("datos.json", "r")
d = json.loads(archivo.read())
archivo.close()

sistema = Sistema()
for item in d["Aviones"]:
    avioncito = Avion()
    avioncito.AsignarAvion(item)
    sistema.AgregarAvion(avioncito)

'''for item in d["Vuelos"]:
    vuelito = Vuelo()
    vuelito.deserializarDniPasajeros(item)
    vuelito.deserializarDniTripulante(item)
'''


for item in d["Personas"]:
    if item["tipo"] == "Pasajero":
        personita = Pasajero()
        personita.deserializarpasajero(item)
        sistema.AgregarPersona(personita)
    elif item["tipo"] == "Servicio":
        personita = Servicio()
        personita.deserializarservicio(item)
        sistema.AgregarPersona(personita)
    elif item["tipo"] == "Piloto":
        personita = Piloto()
        personita.deserializarTripulante(item)



for item in sistema.personas:
    print(item.nombre, item.apellido, item.fecha_nac)


