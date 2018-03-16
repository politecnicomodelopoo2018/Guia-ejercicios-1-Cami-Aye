from Class_alumno import Alumno

unAlumno = Alumno()




#Nota = input("Agregue una nota para %s" %nombre_materia)
#unAlumno.AgregarNotaMateria(nombre, Nota)

#nombre_materia = input("Ingrese el nombre de la nueva materia")
#unAlumno.AgregarMateria(nombre)

for loop in range(10):
    nombre_materia = input("Ingrese nombre de la materia o basta para no agregar mas: ")

    if nombre_materia == "basta":
        break

    unAlumno.AgregarMateria(nombre_materia)
    respuesta = input("Agregar notas?: ")

    if respuesta == "si":

        for loop2 in range(10):
            Nota = input("Agregue una nota para %s o escriba basta para parar: " %nombre_materia)

            if Nota == "basta":
                break

            unAlumno.AgregarNotaMateria(nombre_materia, Nota)




print(unAlumno.listaMateria[0].nombre_materia)
print(unAlumno.listaMateria[0].listaNotas[0])






