from Clase_Alumnos import Alumnos
from Clase_Clientes import Clientes


class Buffet(object):
    def __init__(self):
        self.clientes = []
        self.platos = []
        self.pedidos = []
    #MENUS

    def MenuPrincipal(self):
        print ("Bienvenido al buffet")
        print ("Agregar            1")
        print ("Modificar          2")
        print ("Eliminar           3")
        print ("Listado de platos  4")

    def MenuAgregar(self):
        print ("Opcion Agregar")
        print ("Alumno       1")
        print ("Profesor     2")
        print ("Plato        3")
        print ("Pedido       4")

    def MenuModificar(self):
        print ("Opcion Modificar")
        print ("Alumno         1")
        print ("Profesor       2")
        print ("Plato          3")
        print ("Pedido         4")

    def MenuEliminar(self):
        print ("Opcion Eliminar")
        print ("Alumno        1")
        print ("Profesor      2")
        print ("Plato         3")
        print ("Pedido        4")

    # AGREGAR

    def AgregarAlumno(self, alumno):
        self.clientes.append(alumno)

    def AgregarProfesor(self,profesor):
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

    #MODIFICAR
    def ModificarAlumno(self, alumno, nombre, apellido, division):

        for item_alumno in self.clientes:
            if item_alumno == alumno:
                if nombre != None:
                    item_alumno.SetNombre(nombre)
                if apellido != None:
                    item_alumno.SetApellido(apellido)
                if division != None:
                    item_alumno.SetDivision(division)


    def ModificarProfesor(self, profesor,nombre,apellido, descuento):

        for item_profesor in self.clientes:
            if item_profesor == profesor:
                if nombre != None:
                    item_profesor.SetNombre(nombre)
                if apellido != None:
                    item_profesor.SetApellido(apellido)
                if descuento != None:
                    item_profesor.SetDescuento(descuento)

    def ModificarPlato(self, plato, nombre, precio):

        for item_plato in self.platos:
            if item_plato == plato:
                if nombre != None:
                    item_plato.SetNombre(nombre)
                if precio != None:
                    item_plato.SetPrecio(precio)

    def ModificarPedido(self, pedido, fecha_creacion, plato, persona_que_pidio, hora_entrega, entrega):
        for item_pedido in self.pedidos:
            if item_pedido == pedido:
                if fecha_creacion != None:
                    item_pedido.SetFechaCreacion(fecha_creacion)
                if plato != None:
                    item_pedido.SetPlato(plato)
                if persona_que_pidio != None:
                    item_pedido.SetCliente(persona_que_pidio)
                if hora_entrega != None:
                    item_pedido.SetHoraEntrega(hora_entrega)
                if entrega != None:
                    item_pedido.SetEntrega(entrega)

    #LISTADO PLATOS

    def ListadoPlatos(self, profesor):
        lista_platos = []
        unplato = Plato()
        for item_plato in self.platos:
            unplato.precio = item_plato.precio
            unplato.nombre = item_plato.nombre
            if profesor == True:
                unplato.precio = self.SacarPrecioDescuento(item_plato.precio, profesor.descuento)

            lista_platos.append(unplato)
        return lista_platos



    def SacarPrecioDescuento(self, precio, descuento):
        preciodesc = precio-(precio*descuento)/100
        return preciodesc














