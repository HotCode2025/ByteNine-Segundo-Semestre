#CLASE 5-Tema: Funciones Parte 2 -> Tarea(08-09)
#Punto: 6.2  Ejercicio 11 Agenda Telefonica
#Hacer un programa que simule una Agenda de Contactos.
#Crear un diccionario donde la clave sea el nombre del usuario
#y el valor sea el telefono.
#El programa tendra el siguiente menu de opciones:
#1. Nuevo contacto
#2.Borrar contacto
#3. Ver contactos exixtentes
#4. Salir

num = int(input(
    "Agenda telefonica\n1# Nuevo contacto\n2# Borrar contacto\n3# Ver contactos existentes\n4# Salir\nElige una opcion: "))
agenda = {

}

while True:

    if num == 1:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el telefono del contacto: ")
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado con exito")

    elif num == 2:
        nombre = input("Ingrese el nombre del contacto a borrar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto {nombre} borrado con exito")
        else:
            print("El contacto no existe")

    elif num == 3:
        print(agenda)

    elif num == 4:
        print("Saliendo de la agenda telefonica")
        break

    num = int(input(
        "Agenda telefonica\n1# Nuevo contacto\n2# Borrar contacto\n3# Ver contactos existentes\n4# Salir\nElige una opcion: "))

