# 1: Llenar una lista
#llenar una lista con los números del 1 al 50, luego mostrar
# la lista con el bucle for, los elementos deben mostarse de la siguiente forma:
# 1-2-3-4-5...-50

lista = []
for i in range(1, 51):
    lista.append(i)

for numero in lista:
    if numero < 50:
        print(numero, end="-")
    else:
        print(numero)
