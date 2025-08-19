#Diccionarios
diccionario = {
    "IDE": "Integrated Development Environment",
    "POO": "Programación Orientada a Objetos",
    "SABD": "Sistemas de Administracion de Bases de Datos",
}
print(len(diccionario))  # 3
print(diccionario)
# Acceder a un valor por su clave
print(diccionario["IDE"])
# otra forma de acceder al valor
print(diccionario.get("POO"))
# Modificar un valor
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# como recorrer un diccionario
for termino in diccionario:
    print(termino, ":", diccionario[termino])


for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
# otra manera de recorrer un diccionario
for clave in diccionario.keys():
    print(clave, ":", diccionario[clave])

# comprobar si una clave existe en el diccionario
print("IDE" in diccionario)

# agregar un nuevo elemento
diccionario['PK'] = "Primary Key"
print(diccionario)

# eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# vaciar el diccionario
diccionario.clear()
print(diccionario)  # {}

