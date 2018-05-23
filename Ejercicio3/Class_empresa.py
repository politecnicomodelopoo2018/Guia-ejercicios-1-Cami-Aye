from Class_empleado import Empleado

class Empresa(object):
    nombre = None
    def __init__(self):
        self.listaEmpleados = []


    def AgregarEmpleado (self, nombre):

        unEmpleado = Empleado()
        unEmpleado.nombre = nombre
        self.listaEmpleados.append(unEmpleado.nombre)

