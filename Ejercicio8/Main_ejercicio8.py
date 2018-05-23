from Clase_Programas import Programa
from Ejercicio_Partido.Clase_Persona import Persona
from Clase_Radio import Radio

lista_archivo = []

def CargarAlArchivo(lista):
    archivo = open("archivo_personas.txt" "w")
    for item in lista:
        archivo.write(item.Codificacion())
    archivo.close()
def CargarALista(lista):
    persona = Persona()
    archivo = open("archivo_personas.txt" "r")
    for line in archivo:
        l = line.split("|")
        if l[0] == 'operador_tecnico':
            persona.OperadorTecnico.tipo = l[1]
            persona.OperadorTecnico.nombre = l[2]
            persona.OperadorTecnico.apellido = l[3]
            persona.OperadorTecnico.DNI = l[4]
            persona.OperadorTecnico.fecha_ingreso = l[5]
        elif l[0] == "musicalizador":
            persona.Musicalizador.tipo = l[1]
            persona.Musicalizador.nombre = l[2]
            persona.Musicalizador.apellido = l[3]
            persona.Musicalizador.DNI = l[4]
            persona.Musicalizador.fecha_ingreso = l[5]
        elif l[0] == "conductor":
            persona.Conductor.tipo = l[1]
            persona.Conductor.nombre = l[2]
            persona.Conductor.apellido = l[3]
            persona.Conductor.DNI = l[4]
            persona.Conductor.fecha_ingreso = l[5]
        lista.append(persona)
    archivo.close()

radio = Radio()


while(1):
    opcion = None
    print("1     AgregarPrograma")
    print("2     Agregar Conductor")
    print("3     Agregar Operador Tecnico")
    print("4     Agregar Musicalizador")
    opcion = int(input("Ingrese opcion"))
    if opcion == 1:
        programa = Programa()
        nombre_programa = input("Ingrese nombre del programa: ")
        categoria = input("categoria: ")
        conductor = input("Ingrese nombre_conductor: ")
        operador_tecnico = input("Ingrese nombre del operador_tecnico: ")
        programa.SetNombre(nombre_programa)
        programa.SetCategoria(categoria)
        programa.SetOperadorTecnico(operador_tecnico)
        programa.AgregarConductores(conductor)
        if categoria == "Musica":
            musicalizador = input("Nombre del musicalizador: ")
            estilo_musica = input("Ingrese estilo de musica: ")
            programa.Musicalizador.SetMusicalizador(musicalizador)
            programa.Musicalizador.AgregarEstiloMusica(estilo_musica)
        radio.AgregarPrograma(programa)



