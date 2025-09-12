import math # Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)
#clase 1 " Colecciones (11-08)
#Punto: 1.3 Ejercicio de Tuplas y Listas, mirando la siguiente imagen,
#debes intentar solucionar el ejercicio antes de ver el video con la solución
#Dada la siguiente tupla
#tupla =(13,1,8,3,2,5,8)
#Definimos la tupla
#Crear una lista que solo incluye los numeros menores a 5
# e imprimo por consola (1,2,3)


#Definir tupla
tupla =(13,1,8,3,2,5,8)
#definir lista
lista =[]
#Filtrar los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#CLASE 4-Tema: Ejercicios y Más -> Tarea(01-09)
#Punto:4.4 Ejercicio 1 con Matemáticas y la clase math
#Sacar la raíz cuadrada de un número positivo,
# aquí vamos a seguir aprendiendo, debe quedar claro el trabajo con la clase math...

#Ejercicio para sacar la raiz cuadrada de un numero positivo
numero = int(input('Digite un numero positivo: '))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo:'))
print(f'\n Su raiz cuadrada es: {math.sqrt(numero): .2f}')