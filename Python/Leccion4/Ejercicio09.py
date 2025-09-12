#CLASE 4-Tema: Funciones y Ejercicios -> tarea(01-09)
#Punto: 5.8 Ejercicio 9
#Ejercicio 9: mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usario ingrese una frase, se le
#devolvera la misma frase pero sin espacios en blanco,
# y adeemas un contador de cuantos caracteres tiene la frase
#(sin contar los espacios en blanco)
#Ejemplo: frase = vivir por siempre en paz
#         frase final = vivirporsiempreenpaz
#         N° de caracteres = 20


# Pedir al usuario que ingrese la frase
frase = input("Ingresa una frase: ")

# Eliminamos los espacios en blanco de la frase
fraseSinEspacios = frase.replace(" ", "")#  .replace() busca un caracter (1er argumento) y lo va a remplazar por el segundo


# Contamos la longitud de la nueva frase
longitud = len(fraseSinEspacios)# la funcion len devolvera el numero de caracteres de la frase sera el contador

# Mostrar la frase sin espacios y la longitud
print(f"Frase final: {fraseSinEspacios}")
print(f"N° de caracteres: {longitud}")