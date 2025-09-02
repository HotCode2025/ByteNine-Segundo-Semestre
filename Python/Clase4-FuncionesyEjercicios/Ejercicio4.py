#Sumar numeros pares dentro de un rango
#hacer un programa que sume todos los numeros pares dentro de un rango

rangoMin = int(input("Ingrese el numero minimo del rango: "))
rangoMax = int(input("Ingrese el numero maximo del rango: "))
suma = 0

for numero in range(rangoMin, rangoMax + 1):
    if numero % 2 == 0:
        suma += numero

print(f"La suma de los numeros pares entre {rangoMin} y {rangoMax} es: {suma}")