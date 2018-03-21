import datetime
class Empleado(object):
    nombre = None
    apellido = None
    telefono = None
    fecha_nac = None

    def __init__  (self):
        self.DiasQueAsistir = [True, False, True, True, False, False, True]
        self.DiasAsistidos = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFecha_nacimiento (self, fecha_nacimiento):

        self.fecha_nac = fecha_nacimiento

    def setTelefono (self, telefono):

        self.telefono = telefono

    def DiasAsistidoss (self, año, mes, dia):
        fecha = datetime.date (año, mes, dia)
        self.DiasAsistidos(fecha)

    def NumDiasAsisitidos (self):
        self.DiasAsistidos




