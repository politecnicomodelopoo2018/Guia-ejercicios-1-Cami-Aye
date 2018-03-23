from Class_empleado import Empleado
from Class_empresa import Empresa
import datetime


unEmpleado = Empleado()

unEmpleado.nombre = input("Ingrese el nombre ")
unEmpleado.apellido = input("Ingrese el apellido ")
unEmpleado.telefono = input("Ingrese telefono ")
unEmpleado.fecha_nac = datetime.date(2000,11,29)



while (1):
    cortar_while = None
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    fecha_asistida = datetime.date(año, mes, dia)
    unEmpleado.DiasAsistidoss(fecha_asistida)
    cortar_while = input ("quiere ingresar otra fecha?: ")
    if cortar_while == "no":
        break

SumDias = unEmpleado.NumDiasSemana()
SumDiasAsis = unEmpleado.NumDiasAsisitidos()
promedio = unEmpleado.PromedioDias(SumDias, SumDiasAsis)
print(promedio)

unaEmpresa = Empresa()
unaEmpresa.AgregarEmpleado(unEmpleado.nombre)
print(unaEmpresa.listaEmpleados)