class Empleado(object):
    nombre = None
    apellido = None
    telefono = None
    fecha_nac = None

    def __init__  (self):
        self.DiasQueAsistir = [7]
        self.DiasAsistidos = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFecha_nacimiento (self, fecha_nacimiento):

        self.fecha_nac = fecha_nacimiento

    def setTelefono (self, telefono):
        self.telefono = telefono

    def EstablecerHorario (self, ir):

        self.DiasQueAsistir.append(ir)


    def DiasAsistidosPorMes (self, fue):

        for bool in DiasQueAsistir:

            if bool == True:
                if fue == True:
                    self.DiasAsistidos.append(fue)


    def EncontrarEmpresario (self, nombre):

        for empresario in DiasAsistidos:
            if empresario.nombre == nombre:
                return empresario

    def SumarDiasTrue (self, empresario):
        contador = 0
        for item in DiasQueAsistir:
            if empresario.DiasQueAsistir == True:
                contador +=1
        return contador

    def PromedioPorMes (self, contador):

        promedio = (100*len(self.DiasAsistidos)/contador
        return promedio


