#CLASE 5-Tema: Funciones Recursivas Parte 3  -> Tarea(08-09)
#Punto: 7.7 Ejercicio 5 Funciones (Celsius a Fahrenheit)
#Ejercicio 5: Convertidor de temperaturas
#Realizar dos funciones para convertir de grados celsius
#a fahrenheit y viceversa
#Investigar las formulas

#Función para convertir de Celsius a Fahrenheit
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

#Función para convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

#Menú
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Elegí una opción (1 o 2): ")

if opcion == "1":
    c = float(input("Ingresa la temperatura en °C: "))
    print(f"{c}°C = {celsius_a_fahrenheit(c):.2f}°F")

elif opcion == "2":
    f = float(input("Ingresa la temperatura en °F: "))
    print(f"{f}°F = {fahrenheit_a_celsius(f):.2f}°C")

else:
    print("Opción no válida")
