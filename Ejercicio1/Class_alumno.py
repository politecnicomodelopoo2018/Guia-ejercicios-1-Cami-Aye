from Class_materia import Materia

class Alumno (object):
    nombre = None
    apellido = None
    fecha_nacimiento = None
    def __init__  (self):
        self.listaMateria = []


    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFecha_nacimiento (self, fecha_nacimiento):

        self.fecha_nacimiento = fecha_nacimiento

    def AgregarMateria (self, nombre):
        materia = Materia(nombre)
        self.listaMateria.append(materia)

    def AgregarNotaMateria (self, nombre, nota):

        for buscador in self.listaMateria:

            if buscador.nombre_materia == nombre:
                buscador.setNotas(nota)
                return True









