from Class_empleado import Empleado
import datetime

unEmpleado = Empleado()

unEmpleado.nombre = input("Ingrese el nombre")
unEmpleado.apellido = input("Ingrese el apellido")
unEmpleado.telefono = input("Ingrese telefono")
unEmpleado.fecha_nac = datetime.date(2000,11,29)

for DiasSemana in range(7):
    ir = (bool)input()
    unEmpleado.EstablecerHorario(ir)
