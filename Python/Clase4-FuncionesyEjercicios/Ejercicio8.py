#Ejercicio 8: Menu interactivo - Cajero automático
#Hacer un programa que simule un cajero automitico con un saldo inicial de $1000
#y tendra el siguiente menu de opciones:
#1. Ingresar dinero a la cuenta
#2. Retirar dinero de la cuenta
#3. Mostrar dineros disponible
#4. Salir

#Dejame que lo haga solo por favor

monto = 1000

opcion = int(input("CAJERO AUTOMATICO\n1# Ingresar dinero a la cuenta\n2# Retirar dinero de la cuenta\n3# Mostrar dineros disponible\n4# Salir\nElige una opcion: "))

while opcion != 4:
    if opcion == 1:
        ingreso = float(input("Ingrese la cantidad a depositar: "))
        monto += ingreso
        print(f"Has ingresado ${ingreso}")
    elif opcion == 2:
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > monto:
            print("Fondos insuficientes")
        else:
            monto -= retiro
            print(f"Has retirado ${retiro}")
    elif opcion == 3:
        print(f"El saldo disponible es: ${monto}")
    
    opcion = int(input("CAJERO AUTOMATICO\n1# Ingresar dinero a la cuenta\n2# Retirar dinero de la cuenta\n3# Mostrar dineros disponible\n4# Salir\nElige una opcion: "))

