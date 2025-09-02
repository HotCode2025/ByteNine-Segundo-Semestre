# Eiercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para elle se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos.

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