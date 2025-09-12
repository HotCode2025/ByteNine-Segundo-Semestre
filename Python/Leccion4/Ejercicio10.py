#CLASE 5-Tema: Funciones Parte 2 -> Tarea(08-09)
#Punto: 6.1  Ejercicio 10 No Repetir caracteres
# Ejercicio 10: No repetir caracteres
#Hacer un programa que pida una cadena por teclado, luego
#Meter los caracteres en una lista sin repetir caracteres
def ProgCaracteres():
    print("PROGRAMA DE CARACTERES ÚNICOS")

    while True:
        cadena = input("Introduce una cadena (o 'salir'): ")

        if cadena.lower() == 'salir':
            break

        if not cadena.strip():
            print("Introduce al menos un carácter.")
            continue

        caracteres_unicos = []
        for char in cadena:
            if char not in caracteres_unicos:
                caracteres_unicos.append(char)

        print(f"Cadena: '{cadena}'")
        print(f"Caracteres únicos: {caracteres_unicos}")
        print(f"Total únicos: {len(caracteres_unicos)}")
        print("-" * 30)


# LLAMADA A LA FUNCIÓN - PROGRAMA PRINCIPAL
ProgCaracteres()
