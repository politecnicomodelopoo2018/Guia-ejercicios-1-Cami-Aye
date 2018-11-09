from Mascotas import *
from Duenos import Dueno



dueno = Dueno()
dueno.nombre = "Norma"
dueno2 = Dueno()
pajarito = Pajarito("Pepe", dueno, "Tere")
perro = Perro("Roberto", dueno2)



saludo = pajarito.Saludar(dueno2)
saludo2 = perro.Saludar(dueno2)
print(saludo2)