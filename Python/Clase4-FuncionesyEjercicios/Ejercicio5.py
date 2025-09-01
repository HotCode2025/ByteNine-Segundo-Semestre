# Ejercicio 5: Factorial de un numero positivo
 
num = int(input("Ingresa un numero positvo: "))
if num < 0:
    print("Error: ingresa un numero positivo")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es: {factorial}") 