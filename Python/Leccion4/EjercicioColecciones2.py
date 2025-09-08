#CLASE 4-Tema: Ejercicios y Más -> Tarea(01-09)
#Punto: 4.2  Ejercicio de Colecciones 2
#Ejercicio 2: Operaciones de conjuntos con listas
#Escriba un programa que tenga dos listas y que a continuacion
#cree las siguientes listas( en las que no deben haber repeticion)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no een la segunda
# 3  Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4  Lista de palabras que aparecen en ambas listas

# Definir las dos listas
lista1 = ["Gabriel", "Amelia", "Agustin", "Valeria", "Santiago", "Osvaldo", "Gabriel"]
lista2 = ["Gabriel", "Ariel", "Pamela", "Jadee", "Valentina", "Damian"]

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("-" * 50)

# 1) Lista de palabras que aparecen en las listas (sin repeticion)
todas_palabras = list(set(lista1) | set(lista2))
print("1) Todas las palabras (sin repeticion):")
print(todas_palabras)
print()

# 2) Palabras que aparecen en la primera lista pero no en la segunda
solo_lista1 = list(set(lista1) - set(lista2))
print("2) Palabras solo en la primera lista:")
print(solo_lista1)
print()

# 3) Palabras que aparecen en la segunda lista pero no en la primera
solo_lista2 = list(set(lista2) - set(lista1))
print("3) Palabras solo en la segunda lista:")
print(solo_lista2)
print()

# 4) Palabras que aparecen en ambas listas
en_ambas = list(set(lista1) & set(lista2))
print("4) Palabras en ambas listas:")
print(en_ambas)


