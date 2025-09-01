# Eiercicio 2: Modificar los elementos de una lista
# Llenar una lista con los número del 1 al 10, luego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuario

numeros = [] #Creamos la lista

multiplicador = int(input("Digite un numero: "))

for i in range(10):     #Utilizamos un for para agregar los 10 numeros
    numeros.append(i+1)

print("Lista Original\n",numeros)

for a in range(len(numeros)):

    numeros[a] = numeros[a] * multiplicador

print("\nLista Multiplicada\n",numeros)