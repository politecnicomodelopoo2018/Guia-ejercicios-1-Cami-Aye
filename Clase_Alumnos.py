from Clase_Clientes import Clientes



class Alumnos(Clientes):
    division= None

    def SetNombre(self, nombre):
        self.nombre = nombre

    def SetApellido(self, apellido):
        self.apellido = apellido

    def SetDivision(self, division):
        self.division = division