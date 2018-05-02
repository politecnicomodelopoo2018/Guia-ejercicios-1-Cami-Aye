from Clase_Buffet import Buffet()
from Clase_Clientes import Clientes()
from Clase_Pedidos import Pedidos()
from Clase_Platos import Platos()

opcion = None
buffet = Buffet()
cliente1 =Clientes()
cliente2 =Clientes()
cliente3 =Clientes()
pedido1 = Pedidos()
pedido2 = Pedidos()
pedido3 = Pedidos()
plato1 = Platos()
plato2 = Platos()
plato3 = Platos()

buffet.MenuPrincipal()
opcion = int(input())
if opcion == 1:
    buffet.MenuAgregar()
    opcion2 = None
    opcion2 = int(input())

    if opcion2 == 1:
        cliente1.
    if opcion2 == 2:

    if opcion2 == 3:

    if opcion2 == 4:


if opcion == 2:
    buffet.MenuModificar()
if opcion == 3:
    buffet.MenuEliminar()
if opcion == 4:
    profe = False
    lista = []
    if cliente1.tipo == "profesor":
        profe == True
    lista = buffet.ListadoPlatos(profe)