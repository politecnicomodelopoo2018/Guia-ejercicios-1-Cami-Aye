class Alumno (object):
    nombre = None
    apellido = None
    fecha_nacimiento = None
    def __init__  (self):
        self.listaNotas = []


    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFecha_nacimiento (self, fecha_nacimiento):

        self.fecha_nacimiento = fecha_nacimiento

    def setNotas (self, nota):
        if nota>10:
            return False
        if nota<1:
            return False

        self.listaNotas.append(nota)
        return True


    def mayor (self):
        return max(self.listaNotas)

    def menor (self):
        return min(self.listaNotas)

    def promedio(self):
        if len(self.listaNotas) == 0:
            return False
        posicion = 0
        suma = sum(self.listaNotas)
        for cosito in self.listaNotas:
            posicion+=1
        return suma/posicion



