#CLASE 4-Tema: Funciones y Ejercicios -> tarea(01-09)
#Punto: 5.7 Ejercicio 8
#ejercicio8: Menú interactivo-Cajero automático
#Hacer un programa que simule un cajero automatico con un saldo
#inicial de $ 100 y tendra el siguiente menu de opciones:
#1. Ingresar dinero en la cuenta
#2. Retirar dinero de la cuenta
#3. Mostrar dinero disponible
#4. Salir


saldo = 100
while True:
    print("\n MENU ")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menú: "))

    if opcion == 1:
        ingreso = float(input("Digite la cantidad a ingresar: "))
        saldo += ingreso
        print(f"Usted ingreso : ${ingreso:.2f}")
    elif opcion == 2:
        retiro = float(input("Digite la cantidad a retirar: "))
        if retiro > saldo:
            print("No dispone de esa cantidad de dinero en su cuenta")
        else:
            saldo -= retiro
            print(f"Usted retiro: ${retiro:.2f}")
    elif opcion == 3:
        print(f"Su dinero en la cuenta es: ${saldo:.2f}")
    elif opcion == 4:
        print("Gracias por usar su cajero automatico")
        break
    else:
        print("Opción incorrecta, vuelva a intentarlo")
