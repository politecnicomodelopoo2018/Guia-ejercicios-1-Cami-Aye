
class Radio(object):
    def __init__(self):
        self.programas = []

    def AgregarPrograma(self, programa):
        for item in self.programas:
            if item == programa:
                return False
        self.programas.append(programa)

    def VerificarHorario(self, nombre_programa, horario):
        for item in self.programas:
            if item.nombre == nombre_programa:
                for item2 in item.horarios:
                    if item2 == horario:
                        return False
        return True

