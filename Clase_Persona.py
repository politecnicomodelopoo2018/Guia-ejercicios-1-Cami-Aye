class Persona(object):
    nombre = None
    apellido = None
    DNI = None
    fecha_ingreso = None
    tipo = None


    def SetNombre(self, nombre):
        self.nombre = nombre
    def SetApellido(self, apellido):
        self.apellido = apellido
    def SetDNI (self, DNI):
        self.DNI = DNI
    def SetFechaIngreso(self, fecha_ing):
        self.fecha_ingreso = fecha_ing

    def Codificacion(self):
        return self.tipo + "|" + self.nombre + "|" + self.apellido + "|" + self.DNI + "|" + self.fecha_ingreso + '\n'

