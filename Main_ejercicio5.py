from Clase_canciones import Canciones
from Clase_artistas import Artista
from Clase_discografica import Discografica
from Clase_autores import Autores
from Clase_album import Album



discografica = Discografica()
folie = Album()

folie = input("album nuebooo: ")
discografica.AgregarAlbum(folie)

argentina = input("pais del artista mas influyente: ")
discografica.ListaCancionesPais(argentina)







