#CLASE 4-Tema: Funciones y Ejercicios -> tarea(01-09)
#Punto: 5.6 Ejercicio 7
# Ejercicio 7: Juego adivina el numero
#Realizar un juego para adivinar un numero.Para ello se debe
#generar un numero aleatorio entre 1 -100, y luego ir pidiendo
#numeros indicando "Es mayor" o "es menor" segun sea mayor o menor
#con respecto a N.El proceso termina cuando el usuario acierta
#y alli se debe mostrar el numero de intentos.
import random

print("\tJuego adivina el numero")
aleatorio = random.randint(0,100)#Toma de 0 a 100 literal, generamos un numero aleatorio
contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\t No es el numero, digite un numero menor")
    elif numero < aleatorio:
        print("\tNo es el numero, digite un numero mayor")
    else:
        print(f"Felicitaciones, adivino el numero {aleatorio}")
        break#Rompemos el ciclo
print(f"\nNumeros digitados hasta adivinar: {contador}")