from Clase_Programas import Programa
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000from Clase_Persona import Persona
from Clase_Radio import Radio


def CargarArchivoLista(self):
    datos = []
    archivo_personas = open('Archivo_Personas.txt', 'r')
    for line in archivo_personas:
        datos = line.split("/")


def BuscarEnArchivo(self, nombre_persona, apellido_persona, tipo):
    datos = []
    archivo_personas = open('Archivo_Personas.txt', 'r')
    for line in archivo_personas:
        datos = line.split("/")
        if datos[1] == nombre_persona and datos[2] == apellido_persona and datos[0] == tipo:
            return datos
            archivo_personas.close()
    archivo_personas.close()
    return True


radio = Radio()



while(1):
    print ("1   Agregar Programas"
           "2   Agregar Conductores"
           "3   Agregar Musicalizadores"
           "4   Agregar Operadores Tecnicos")
    opcion = int(input("Ingrese un numero"))
    if opcion == 1:
        programa = Programa()
        persona = Persona()
        print("Ingrese nombre del programa, categoria y nombre y apellido del operador tecnico")
        nombre_programa = input()
        categoria = input()
        nombre_operador = input()
        apellido_operador = input()

        tipo = "operador_tecnico"
        if persona.BuscarEnArchivo(nombre_operador, apellido_operador, tipo) == True:
            print ("El operador tecnico no existe")
            break
        operador_tecnico = nombre_operador + " " + apellido_operador
        programa.SetOperadorTecnico(operador_tecnico)

        while(1):
            nombre_conductor = input("Ingrese nombre del conductor")
            apellido_conductor = input("Ingrese el apellido del conductor")
            tipo = "conductor"
            if persona.BuscarEnArchivo(nombre_conductor,apellido_conductor, tipo) == True:
                print ("El conductor no existe")
                break
            conductor = nombre_conductor + " " + apellido_conductor
            if programa.AgregarConductores(conductor) == False:
                print("El conductor ya existe")
                break
            programa.AgregarConductores(conductor)

            horario = input("Ingrese el horario de transmision")
            if programa.AgregarHorario(horario) == False:
                print("El horario ya existe")
                break
            programa.AgregarHorario(horario)
            if programa.categoria == "Musica":
                nombre_musicalizador = input("  Ingrese nombre musicalizador")
                apellido_musicalizador = input("Ingrese apellido musicalizador")
                tipo = "musicalizador"
                if persona.BuscarEnArchivo(nombre_musicalizador, apellido_musicalizador, tipo) == True:
                    print ("El musicalizador no existe")
                    break
                musicalizador = nombre_musicalizador + " " + apellido_musicalizador
                programa.Musica.SetMusicalizador(musicalizador)
                salir =     True
                while(salir):
                    estilo = input("Ingrese un estilo de musica para el programa o escriba basta")
                    if estilo == "basta":
                        break
                    programa.Musica.AgregarEstiloMusica(estilo)
                radio.AgregarPrograma(programa.Musica)
            elif categoria != "Musica":
                radio.AgregarPrograma(programa)

    if opcion == 2:
        persona = Persona()
        nombre_conductor = input("Ingrese nombre del conductor")
        apellido_conductor = input("Ingrese apellido del conductor")
        DNI = input("Ingrese DNI del conductor")
        fecha_ingreso = input("Ingrese fecha de ingreso del conductor")
        tipo = "conductor"
        if persona.BuscarEnArchivo(nombre_conductor, apellido_conductor, tipo) != True:
            print("el conductor ya existe")
            break
        persona.Conductor.SetNombre(nombre_conductor)
        persona.Conductor.SetApellido(apellido_conductor)
        persona.Conductor.SetDNI(DNI)
        persona.Conductor.SetFechaIngreso(fecha_ingreso)
        persona.AgregaraArchivoPersonas(persona.Conductor)

    if opcion == 3:
        persona = Persona()
        nombre_musicalizador = input("Ingrese nombre del musicalizador")
        apellido_musicalizador = input("Ingrese apellido del musicalizador")
        DNI = input("Ingrese DNI del musicalizador")
        fecha_ingreso = input("Ingrese fecha de ingreso del musicalizador")
        tipo = "musicalizador"
        if persona.BuscarEnArchivo(nombre_musicalizador, apellido_musicalizador, tipo) != True:
            print("el musicalizador ya existe")
            break
        persona.Musicalizador.SetNombre(nombre_musicalizador)
        persona.Musicalizador.SetApellido(apellido_musicalizador)
        persona.Musicalizador.SetDNI(DNI)
        persona.Musicalizador.SetFechaIngreso(fecha_ingreso)
        persona.AgregaraArchivoPersonas(persona.Musicalizador)
    if opcion == 4:
        persona = Persona()
        nombre_operador = input("Ingrese nombre del operador")
        apellido_operador = input("Ingrese apellido del operador")
        DNI = input("Ingrese DNI del operador")
        fecha_ingreso = input("Ingrese fecha de ingreso del operador")
        tipo = "operador_tecnico"
        if persona.BuscarEnArchivo(nombre_operador, apellido_operador, tipo) != True:
            print("el operador ya existe")
            break
        persona.OperadorTecnico.SetNombre(nombre_operador)
        persona.OperadorTecnico.SetApellido(apellido_operador)
        persona.OperadorTecnico.SetDNI(DNI)
        persona.OperadorTecnico.SetFechaIngreso(fecha_ingreso)
        persona.AgregaraArchivoPersonas(persona.OperadorTecnico)

    break










