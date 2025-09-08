
#CLASE 4-Tema: Ejercicios y Más -> Tarea(01-09)
#Punto: 4.6 Ejercicio 1 Llenar una Lista
#Ejercicio 1: Llenar una lista con los numeros del 1 al 50,luego mostrar
#la lista con un bucle for, los elementos deben mostrarse
#de la siguiente forma:
#1-2-3-4-5...-50

lista = []
for i in range(1, 51):
    lista.append(i)

for numero in lista:
    if numero < 50:
        print(numero, end="-")
    else:
        print(numero)
