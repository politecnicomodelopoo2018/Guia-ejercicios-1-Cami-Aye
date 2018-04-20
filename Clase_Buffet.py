from Clase_Alumnos import Alumnos
from Clase_Clientes import Clientes


class Buffet(object):
    def __init__(self):
        self.clientes = []
        self.platos = []
        self.pedidos = []

    # AGREGAR
    def AgregarAlumnos(self, alumno):
        self.clientes.append(alumno)

    def AgregarProfesores(self, profesor):
        self.clientes.append(profesor)

    def AgregarPlatos(self, plato):
        self.platos.append(plato)

    def AgregarPedidos(self, pedido):
        self.pedidos.append(pedido)

    # ELIMINAR
    def EliminarAlumno(self, alumno_eliminado):
        for item in self.clientes:
            if item == alumno_eliminado:
                self.clientes.remove(item)
                break

    def EliminarProfesor(self, profesor_eliminado):
        for item in self.clientes:
            if item == profesor_eliminado:
                self.clientes.remove(item)
                break

    def EliminarPlato(self, plato_eliminado):
        for item in self.platos:
            if item == plato_eliminado:
                self.platos.remove(item)
                break

    def EliminarPedido(self, pedido_eliminado):
        for item in self.pedidos:
            if item == pedido_eliminado:
                self.pedidos.remove(item)
                break
