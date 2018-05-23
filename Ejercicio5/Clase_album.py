class Album(object):
    titulo = None

    def __init__(self):
        self.canciones = []

    def SetTitulo(self, titulo):
        self.titulo = titulo

    def AgregarCanciones(self, cancion):
        self.canciones.append(cancion)

    # Artista mas influyente del album
    def MasInfluyente(self):
        artista_mas_influyente = None
        artista_normal = None
        contador_canciones_aparicion = None
        contador
        _top_aparicion = None
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

    # Listado artistas que participaron en un album
    def ArtistasParticipantes(self):
        participantes = []
        for item in self.canciones:
            for item2 in item.artistas:
                if item2 not in participantes:
                    participantes.append(item2)
        return participantes
