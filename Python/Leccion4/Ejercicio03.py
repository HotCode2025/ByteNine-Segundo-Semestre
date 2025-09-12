#CLASE 4-Tema: Ejercicios y Más -> Tarea(01-09)
#Punto: 4.8 Ejercicio 3 Insertar Elementos y Ordenarlos Función sort(),
# este ejercicio se los dejo para que tengan claro el trabajo con la función sort...
#Ejercicio 3: Pedir numeros y meterlos en una lista, cuando el usuario
#introduzca un numero 0, nuestro programa dejaria de insertar.
#Por ultimo, mostrar los numeros ordenados de menor a mayor.

lista = []
salir = False#bandera
while not salir:
    numero = int(input('Digite un numero: '))
    if numero ==0:
        salir = True
    else:
        lista.append(numero)
#funcion para ordenar
lista.sort()# la lista esta ordenada con esta funcion
print(f'Lista ordenada; \n{lista}')

