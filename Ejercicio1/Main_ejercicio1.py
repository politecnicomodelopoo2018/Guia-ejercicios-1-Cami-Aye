from Class_alumno import Alumno
import datetime

alumnito1 = Alumno()

nombre = input("Ingrese su nombre: ")
alumnito1.setNombre(nombre)

apellido = input("Ingrese su apellido: ")
alumnito1.setApellido(apellido)

bday = datetime.date(2000, 8, 4)
alumnito1.setFecha_nacimiento(bday)

# print (alumnito1.nombre)
print (alumnito1.apellido)
print (alumnito1.fecha_nacimiento)

Nota = int(input("Agregue nota"))
alumnito1.setNotas(Nota)
Nota2 = int(input("Agregue nota"))
alumnito1.setNotas(Nota2)

mayor = alumnito1.mayor()
print ("Nota %s" %mayor)


menor = alumnito1.menor()
print ("Nota %s" %menor)

promedio = alumnito1.promedio()
print ("Nota %s" %promedio)
