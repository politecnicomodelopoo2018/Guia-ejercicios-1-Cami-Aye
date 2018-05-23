from Clase_canciones import Canciones
from Clase_artistas import Artista
from Clase_discografica import Discografica
from Clase_autores import Autores
from Ejercicio5.Clase_album import Album



discografica = Discografica()
album = Album()


cancion = Canciones()
cancion2 = Canciones()
cancion3 = Canciones()
cancion4 = Canciones()

artista = Artista()
artista2 = Artista()
artista3 = Artista()
artista4 = Artista()
artista5 = Artista()
autor = Autores()
autor2 = Autores()
autor3 = Autores()
album.titulo = input("albun nuebooo xddd: ")
discografica.AgregarAlbum(album)

argentina = input("pais del artista mas influyente: ")
discografica.ListaCancionesPais(argentina)

cancion.titulo = input("Titulo de la cancion: ")
album.AgregarCanciones(cancion)

for item in range(5):
    nombre_artista = input("Artista a a a a: ")
    artista.SetNombre(nombre_artista)
    cancion.AgregarArtistas(artista)
for item in range(3):
    nombre_autor = input("Autor: ")
    autor.SetNombre(nombre_autor)


cancion.AgregarAutores(autor)


print (autor.nombre)












