from Class_empleado import Empleado
import datetime

unEmpleado = Empleado()

unEmpleado.nombre = input("Ingrese el nombre ")
unEmpleado.apellido = input("Ingrese el apellido ")
unEmpleado.telefono = input("Ingrese telefono ")
unEmpleado.fecha_nac = datetime.date(2000,11,29)

for DiasSemana in range(7):
    dia = 1
    ir = None
    varchar = input("Ingrese el horario, dia ")
    if varchar != "1" and varchar != "0":
        while(1):
            varchar = input("Ingrese un 1 o un 0: ")
            if varchar == "1" or varchar == "0":
                break
    if varchar == "1":
        ir = True
    elif (varchar == "0"):
        ir = False


    unEmpleado.EstablecerHorario(ir)
    dia+=1

contador_dias = unEmpleado.SumarDiasTrue(unEmpleado)
print (contador_dias)

for DiasQueAsistio in range(28):


