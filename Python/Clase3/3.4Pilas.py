# Metodo: Pilas usando lista
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos por el final
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo así: {pila}')
