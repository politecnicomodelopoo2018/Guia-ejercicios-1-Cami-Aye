from Clase_Clientes import Clientes

class Profesor (Clientes):
    descuento = None
    def SetDescuento(self, desc):
        self.descuento = desc