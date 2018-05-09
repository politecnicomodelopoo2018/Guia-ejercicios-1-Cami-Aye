from Clase_Buffet import Buffet
from Clase_Clientes import Clientes
from Clase_Pedidos import Pedidos
from Clase_Platos import Platos
import datetime

opcion = None
buffet = Buffet()

buffet.MenuPrincipal()
opcion = int(input())
if opcion == 1:
    buffet.MenuAgregar()
    opcion2 = None
    opcion2 = int(input())

    if opcion2 == 1:
        while(1):
            cerrar = None

            cliente = Clientes()
            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Su apellido: ")
            division = input("A que division pertenece: ")

            if buffet.BuscarCliente(nombre, apellido, False) == True:
                print("El cliente ya existe")
                break

            cliente.alumno.SetNombre(nombre)
            cliente.alumno.SetApellido(apellido)
            cliente.alumno.SetDivision(division)
            buffet.AgregarAlumno(cliente)

            cerrar = input("Ingresar otro alumno?")
            if cerrar == "no" or cerrar == "No":
                break

    if opcion2 == 2:
        while (1):
            cerrar = None
            cliente = Clientes()

            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Su apellido: ")
            descuento = input("Establezca el descuento: ")

            if buffet.BuscarCliente(nombre, apellido, False) == True:
                print("El cliente ya existe")
                break

            cliente.profesor.SetDescuento(descuento)
            cliente.profesor.SetNombre(nombre)
            cliente.profesor.SetApellido(apellido)
            buffet.AgregarProfesor(cliente)

            cerrar = input("Ingresar otro alumno?")
            if cerrar == "no" or cerrar == "No":
                break

    if opcion2 == 3:
        while(1):
            cerrar = None
            plato = Platos()

            nombre = input("Nombre del plato: ")
            precio = input("Precio: ")

            if buffet.BuscarPlato(nombre, False) == True:
                print("El plato ya existe")
                break

            plato.SetNombre(nombre)
            plato.SetPrecio(precio)
            buffet.AgregarPlatos(plato)

            cerrar = input("Ingresar otro alumno?")
            if cerrar == "no" or cerrar == "No":
                break

    if opcion2 == 4:
        while(1):
            cerrar = None
            pedido = Pedidos()

            fecha = input("Ingrese fecha: ")
            fecha = datetime.strptime(fecha, '%dd/%mm/%Y')
            plato = input("Nombre del plato: ")
            if buffet.BuscarPlato(plato, False) == False:
                print("El plato no existe")
                break
            nombre_Cliente = input("Nombre del cliente: ")
            apellido_Cliente = input("Apellido: ")
            if buffet.BuscarCliente(nombre_Cliente, apellido_Cliente, False) == False:
                print ("El cliente no existe")
                break
            hora_de_entrega = input("Hora programa de entrega: ")
            entregado = input("¿Se entrego el pedido?: ")

            pedido.SetFechaCreacion(fecha)
            pedido.SetPlato(plato)
            pedido.SetCliente(nombre_Cliente+" "+apellido_Cliente)
            pedido.HoraEntrega(hora_de_entrega)
            pedido.SetEntrega(entregado)






































































































































































































































































































































































































































































































































































































































































































































            if buffet.BuscarPedido(pedido) == True:
                print("El pedido ya existe")
                break

            buffet.AgregarPedidos(pedido)

            cerrar = input("Ingresar otro alumno?")
            if cerrar == "no" or cerrar == "No":
                break

if opcion == 2:
    buffet.MenuModificar()
    opcion2 = int(input())

    if opcion2 == 1:
        while(1):
            cerrar = None

            nombre_a_modificar = input("Ingrese nombre del alumno a modificar: ")
            apellido_a_modificar = input("Apellido del alumno a modificar: ")

            alumno_a_modificar = buffet.BuscarCliente(nombre_a_modificar, apellido_a_modificar, True)
            if alumno_a_modificar == False:
                print("El alumno que desea modificar no existe")
                break

            if alumno_a_modificar != True:
                nombre_nuevo = input("Ingrese el nombre nuevo: ")
                apellido_Nuevo = input("Nuevo apellido: ")
                division_nueva = input("Ingrese la nueva division: ")
                buffet.ModificarAlumno(alumno_a_modificar, nombre_nuevo, apellido_Nuevo, division_nueva)



        if opcion2 == 2:
            while (1):
                cerrar = None

                nombre_a_modificar = input("Ingrese nombre del profesor a modificar: ")
                apellido_a_modificar = input("Apellido del profesor a modificar: ")
                profesor_a_modificar = buffet.BuscarCliente(nombre_a_modificar, apellido_a_modificar, True)
                if profesor_a_modificar == False:
                    print("El profesor que desea modificar no existe")
                    break
                if profesor_a_modificar != True:
                    nombre_nuevo = input("Ingrese el nombre nuevo: ")
                    apellido_Nuevo = input("Nuevo apellido: ")
                    descuento_nuevo = int(input("Ingrese descunto nuevo: "))
                    buffet.ModificarProfesor(profesor_a_modificar, nombre_nuevo, apellido_Nuevo, descuento_nuevo)
                cerrar = input("Ingresar otro alumno-?")
                if cerrar == "no" or cerrar == "No":
                    break
        if opcion2 == 3:
            while(1):
                cerrar = None
                nombre_plato_a_modificar = input("Ingrese el nombre del plato a modificar: ")

                plato_a_modificar = buffet.BuscarPlato(nombre_plato_a_modificar, True)
                if plato_a_modificar == False:
                    print("El plato que desea modificar no existe")
                    break
                if plato_a_modificar != True:
                    nombre_nuevo = input("Ingrese el nombre nuevo del plato")
                    precio = int(input("Ingrese el precio nuevo: "))
                    buffet.ModificarPlato(plato_a_modificar, nombre_nuevo, precio)

                cerrar = input("Ingresar otro alumno-?")
                if cerrar == "no" or cerrar == "No":
                    break

        if opcion2 == 4:
            cerrar = None
            plato_modificar = input("Ingrese plato del pedido a modificar")
            persona_modifcar = input("Ingrese el cliente del pedido a modificar")

            fecha_modificar = input("Ingresela fecha del pedido a modificar: ")
            pedido_a_modificar = buffet.BuscarPlato(nombre_pedido_a_modificar, True)
            if pedido_a_modificar == False:
                print ("El pedido que desea modificar no existe")
                break
            if pedido_a_modificar != True




if opcion == 3:
    buffet.MenuEliminar()
if opcion == 4:
    profe = False
    lista = []
    if cliente1.tipo == "profesor":
        profe == True
    lista = buffet.ListadoPlatos(profe)