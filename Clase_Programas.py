class Programa(object):
    nombre = None
    categoria = None
    operador_tecnico = None
    def __init__(self):
        self.conductores = []
        self.horarios = []

    def SetNombre(self, nombre):
        self.nombre = nombre
    def SetCategoria(self, categoria):
        self.categoria = categoria
    def SetOperadorTecnico(self, persona):
        self.operador_tecnico = persona
    def AgregarConductores (self, conductor):
        for item in self.conductores:
            if conductor == item:
                return False
        self.conductores.append(conductor)
    def AgregarHorario(self, horario):
        for item in self.horarios:
            if item == horario:
                return False
        self.horarios.append(horario)
