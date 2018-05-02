from Clase_Clientes import Clientes



class Alumnos(Clientes):
    division= None

    def SetDivision(self, division):
        self.division = division