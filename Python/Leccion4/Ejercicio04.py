#CLASE 4-Tema: Funciones y Ejercicios -> tarea(01-09)
#Punto: 5.1 Ejercicio 4 Sumar Números pares dentro de un rango
#Ejercicio 4: Sumar numeros pares dentro de un rango
#Hacer un programa para sumar numeros pares dentro de un rango, por ejemplo:
#suma de numeros pares del 2 al 30
#suma =240

rangoMin = int(input("Ingrese el numero minimo del rango: "))
rangoMax = int(input("Ingrese el numero maximo del rango: "))
suma = 0

for numero in range(rangoMin, rangoMax + 1):
    if numero % 2 == 0:
        suma += numero

print(f"La suma de los numeros pares entre {rangoMin} y {rangoMax} es: {suma}")