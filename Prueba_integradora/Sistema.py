class Sistema(object):

    def __init__(self):
        self.duenos = []
        self.mascotasTotales = []

    def AgregarDueno(self, dueno):
        self.duenos.append(dueno)

    def AgregarMascotas(self, mascota):
        self.mascotasTotales.append(mascota)