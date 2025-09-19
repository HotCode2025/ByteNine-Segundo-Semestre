#CLASE 5-Tema: Funciones Parte 2 -> Tarea(08-09)
#Punto: 6.9.1 Ejercicio Funciones 01
#Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
#numerico, utilizando argumentos variables *args como parametro de la
#Funcion y agregar como resultado la suma de todos los valores pasados
#como argumentos 

def sumar(*args):
    return sum(args)

resultado = sumar(5,5,10,20)

print(f"La suma es: {resultado}")