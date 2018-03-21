class Empleado(object):
    nombre = None
    apellido = None
    telefono = None
    fecha_nac = None

    def __init__  (self):
        self.DiasQueAsistir = []
        self.DiasAsistidos = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFecha_nacimiento (self, fecha_nacimiento):

        self.fecha_nac = fecha_nacimiento

    def setTelefono (self, telefono):
        self.telefono = telefono




