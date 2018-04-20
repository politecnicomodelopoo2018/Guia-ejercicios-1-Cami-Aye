class Album(object):
    titulo = None

    def __init__(self):
        self.canciones = []

    def SetTitulo(self, titulo):
        self.titulo = titulo

    def AgregarCanciones(self, cancion):
        self.canciones.append(cancion)

    def MasInfluyente(self):
        artista_mas_influyente = None
        artista_normal = None
        contador_canciones_aparicion = None
        contador_top_aparicion = None
        for item in self.canciones:
            for item2 in item.artistas:
                artista_normal = item2
                for item3 in self.canciones:
                    for item4 in item3.artistas:
                        if artista_normal == item4:
                            contador_canciones_aparicion += 1
                if contador_canciones_aparicion > contador_top_aparicion:
                    contador_top_aparicion = contador_canciones_aparicion
                    artista_mas_influyente = artista_normal
                    contador_canciones_aparicion = 0
        return artista_mas_influyente


    def ArtistasParticipantes(self):
        participantes = []
        for item in self.canciones:
            for item2 in item.artistas:
                participantes.append(item2)
        return participantes
