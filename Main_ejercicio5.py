from Clase_canciones import Canciones
from Clase_artistas import Artista
from Clase_discografica import Discografica
from Clase_autores import Autores
from Clase_album import Album



discografica = Discografica()
album = Album()
cancion = Canciones()
artista = Artista()
autor = Autores()
album.titulo = input("albun nuebooo xddd: ")
discografica.AgregarAlbum(album)

argentina = input("pais del artista mas influyente: ")
discografica.ListaCancionesPais(argentina)

cancion.titulo = input("Titulo de la cancion: ")
album.AgregarCanciones(cancion)

artista.nombre = input("Artista a a a a: ")
autor.nombre = input("Autor: ")
cancion.AgregarArtistas(artista)
cancion.AgregarAutores(autor)











