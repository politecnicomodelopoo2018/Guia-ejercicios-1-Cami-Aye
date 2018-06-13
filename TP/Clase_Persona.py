class Persona(object):
    nombre = None
    apellido = None
    fecha_nac = None
    DNI = None

    def deserializartipo(self, persona):
        self.nombre = persona["nombre"]
        self.apellido = persona["apellido"]
        self.fecha_nac = persona["fechaNacimiento"]
        self.DNI = persona["dni"]