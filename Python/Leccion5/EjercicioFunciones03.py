#CLASE 5-Tema: Funciones Recursivas Parte 3  -> Tarea(08-09)
#Punto: 7.5 Ejercicio 3
# Ejercicio 3: Funcion recursiva
#Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
def imprimir_descendente(n):
    #Si n <= 0, no imprime nada
    if n <= 0:
        return
    #Imprimir el número actual
    print(n)
    #Llamada recursiva con n - 1
    imprimir_descendente(n - 1)


#Programa principal
numero = int(input("Ingrese un número positivo: "))
imprimir_descendente(numero)
