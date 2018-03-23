import datetime
class Empleado(object):
    nombre = None
    apellido = None
    telefono = None
    fecha_nac = None

    def __init__  (self):
        self.Mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
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

    def DiasAsistidoss (self, fecha):
        self.DiasAsistidos.append(fecha)

    def NumDiasAsisitidos (self):
        SumDiasAsis = 0
        for dia in self.DiasAsistidos:
            diasemana = dia.weekday()
            print(diasemana)
            if self.DiasQueAsistir[diasemana] == True:
                SumDiasAsis+=1

        return SumDiasAsis

    def NumDiasSemana (self):
        SumDias = 0
        for dia in self.DiasQueAsistir:
            if dia == True:
                SumDias += 1
        return SumDias*4

    def PromedioDias (self, SumDias, SumDiasAsis):
        promedio = float((SumDiasAsis*100)/SumDias)
        return promedio



