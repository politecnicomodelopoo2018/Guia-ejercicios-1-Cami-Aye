from Class_empleado import Empleado
from Class_empresa import Empresa
import datetime


unEmpleado = Empleado()

unEmpleado.nombre = input("Ingrese el nombre ")
unEmpleado.apellido = input("Ingrese el apellido ")
unEmpleado.telefono = input("Ingrese telefono ")
unEmpleado.fecha_nac = datetime.date(2000,11,29)
unaempresa = Empresa

unaEmpresa = Empresa()
unaempresa.AgregarEmpleado(unEmpleado.nombre)





