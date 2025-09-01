# Ejercicio 6: Tabla de Multiplicar
# Hacer un programa que pida un número (1 al 10 ) por teclado y guarde en una lista
# su tabla de multiplicar 

# Pedimos un número por teclado
numero = int(input("Ingrese un número (del 1 al 10) para mostrar su tabla de multiplicar : "))

# Creamos la lista con la tabla de multiplicar del 1 al 10
tabla_multiplicar = []
for i in range(1, 11):
    resultado = numero * i
    tabla_multiplicar.append(resultado)

# Mostramos la tabla
print(f"\nTabla de multiplicar del {numero}: ")
print(tabla_multiplicar)
