from Class_empleado import Empleado

class Empresa(object):
    def __init__(self):

        listaEmpleados = []


    def SetEmpleado (self, nombre):

        unEmpleado = Empleado(nombre)
        self.listaEmpleados.append(unEmpleado)

