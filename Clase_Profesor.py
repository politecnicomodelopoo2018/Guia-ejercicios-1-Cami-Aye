from Clase_Clientes import Clientes

class Profesor (Clientes):
    descuento = None

    def SetNombre(self, nombre):
        self.nombre = nombre

    def SetApellido(self, apellido):
        self.apellido = apellido

    def SetDescuento(self, desc):
        self.descuento = desc