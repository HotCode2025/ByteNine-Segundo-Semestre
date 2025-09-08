#CLASE 4-Tema: Ejercicios y Más -> Tarea(01-09)
#Punto: 4.1  Ejercicio de Colecciones 1
#Tarea:  hacer los ejercicios sin tener el video. (entrega antes de 23 hs)
#Ejercicio 1: Eliminar duplicacion de una lista
#Escriba u programa donde tenga una lista y que a continuacion 
#elimine los elementos repetidos, por ultimo mostrar la lista

#Creamos una lista
# Creamos la lista con elementos duplicados
lista = [987, 289, 310, 500, 476, 289, 569, 310, 500]

# Creamos una lista vacía para almacenar los elementos sin duplicados
listaSinDuplicados = []

# Usamos un ciclo for para iterar cada elemento de la lista creadaque es la original
for elemento in lista:
    # con sentencia if me aseguro que el elemento no esta en la lista
    if elemento not in listaSinDuplicados:
        listaSinDuplicados.append(elemento) # Al comprar que no esta, se agrega a la nueva lista

print("Esta es la lista original:", lista)
print("Esta es la lista sin duplicados:", listaSinDuplicados)

