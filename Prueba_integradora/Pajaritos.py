class Pajarito(object):
    nombre = None
    saludo = "Pio"
    canto = None
    tipo = "Pajarito"

    def SetPajarito(self, nombre, canto):
        self.nombre = nombre
        self.canto = canto

    def ModificarPajarito(self, nombre_nuevo, canto_nuevo):
        self.nombre = nombre_nuevo
        self.canto = canto_nuevo