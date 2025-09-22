#CLASE 5-Tema: Funciones Recursivas Parte 3  -> Tarea(08-09)
#Punto: 7.1 Ejercicio 2 con funciones y argumentos variables
#resolviendo dudas

def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

print(multiplicar(2, 3))
print(multiplicar(1, 2, 3, 7))