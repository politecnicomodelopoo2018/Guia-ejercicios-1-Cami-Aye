class Persona(object):
    nombre = None
    apellido = None
    DNI = None
    fecha_ingreso = None
    tipo = None

    def SetNombre(self, nombre):
        self.nombre = nombre
    def SetApellido(self, apellido):
        self.apellido = apellido
    def SetDNI (self, DNI):
        self.DNI = DNI
    def SetFechaIngreso(self, fecha_ing):
        self.fecha_ingreso = fecha_ing
    def AgregaraArchivoPersonas(self, persona):
        datos = self.BuscarEnArchivo(persona.nombre, persona.apellido)
        if datos == True:
            archivo_personas = open('Archivo_Personas.txt', 'w')
            archivo_personas.write(persona.tipo + "/" + persona.nombre + "/" + persona.apellido + "/" + persona.DNI + "/" + persona.fecha_ingreso + "\n")
            archivo_personas.close()
        return False
