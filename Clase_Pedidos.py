class Pedidos (object):
    fecha_creacion = None
    plato = None
    persona_que_pidio = None
    hora_entrega = None
    entrega = None

    def SetFechaCreacion(self,fecha):
        self.fecha_creacion = fecha

    def SetPlato(self, plato):
        self.plato =  plato

    def SetCliente(self,persona):
        self.persona_que_pidio = persona

    def SetHoraEntrega(self,hora):
        self.hora_entrega = hora

    def SetEntrega(self, entregado):
        if entregado == True:
            self.entrega = "si"
        if entregado == False:
            self.entrega = "no"