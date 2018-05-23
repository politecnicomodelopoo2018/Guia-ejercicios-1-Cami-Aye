from Clase_Persona import Persona
persona = Persona()



diccionario = {"Personas":[{"nombre":"", "apellido":"", "edad":""}]}

nombre = "Juan"
apellido = "Lopez"
edad = 10
diccionario['Personas'].append({"nombre":nombre, "apellido":apellido, "edad":edad})

print(diccionario["Personas"][0]['nombre'][0]["apellido"])

