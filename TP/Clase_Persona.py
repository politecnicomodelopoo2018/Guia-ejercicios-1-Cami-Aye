class Persona(object):
    nombre = None
    apellido = None
    fecha_nac = None
    DNI = None
    tipo = None

    def deserializartipo(self, persona):
        self.tipo = persona["tipo"]
        self.nombre = persona["nombre"]
        self.apellido = persona["apellido"]
        self.fecha_nac = persona["fechaNacimiento"]
        self.DNI = persona["dni"]