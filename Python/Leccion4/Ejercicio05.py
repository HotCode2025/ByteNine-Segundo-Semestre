#CLASE 4-Tema: Funciones y Ejercicios -> tarea(01-09)
#Punto: 5.2 Ejercicio 5 Factorial de un número positivo
# Ejercicio 5: Factorial de un numero positivo
#Hacer un programa para calcular el factorial de un numero positivo
num = int(input("Ingresa un numero positvo: "))
if num < 0:
    print("Error: ingresa un numero positivo")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es: {factorial}")