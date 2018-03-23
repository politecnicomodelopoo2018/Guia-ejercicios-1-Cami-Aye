from Class_empleado import Empleado
from Class_empresa import Empresa
import datetime


unEmpleado = Empleado()

unEmpleado.nombre = input("Ingrese el nombre ")
unEmpleado.apellido = input("Ingrese el apellido ")
unEmpleado.telefono = input("Ingrese telefono ")
dia_nac = int(input("Ingrese dia de su nacimiento: "))
mes_nac = int(input("Ingrese mes de su nacimiento: "))
año_nac = int(input("Ingrese año de su nacimiento: "))
fecha_nac = datetime.date(año_nac, mes_nac, dia_nac)
unEmpleado.setFecha_nacimiento(fecha_nac)


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

mes = int(input("De que mes quiere sacar el promedio?"))
año = int(input("De que año quiere sacar el promedio?"))
SumDias = unEmpleado.NumDiasSemana(mes, año)
SumDiasAsis = unEmpleado.NumDiasAsisitidos()
promedio = unEmpleado.PromedioDias(SumDias, SumDiasAsis)
print(promedio)

unaEmpresa = Empresa()
unaEmpresa.AgregarEmpleado(unEmpleado.nombre)
print(unaEmpresa.listaEmpleados)