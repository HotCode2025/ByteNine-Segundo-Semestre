#CLASE 4-Tema: Funciones y Ejercicios -> tarea(01-09)
#Punto: 5.6 Ejercicio 7
#Ejercicio 7: Juego adivina el numero
#Realizar un juego de adivinar un numero.Para ello se debe
#generar un numero aleatorio entre 1-100, y luego ir pidiendo 
# números indicando "es mayor" o "es menor" segun sea mayor o menor
#con respecto a N. El proceso termina cuando el usuario acierta
# y alli debe mostrar el numero de intentos.

import random

aleatorio = random.randint(1, 100)

intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Ingrese su número: "))
    intentos += 1

    if intento < aleatorio:
        print("El número es mayor")
    elif intento > aleatorio:
        print("El número es menor")
    else:
        adivinado = True
        print(f"¡Correcto! El número era {aleatorio}.")
        print(f"Lo lograste en {intentos} intentos.")