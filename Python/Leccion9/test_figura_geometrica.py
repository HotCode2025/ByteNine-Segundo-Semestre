# Clase 9 POO Parte 5 Herencia Múltiple Tarea
# 12.4 Creamos la clase para testear nuestro código

from Cuadrado import Cuadrado

cuadrado1 =Cuadrado(5, 'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Calculo del área del cuadrado: {cuadrado1.calcular_area()}')

# 12.5 Explicación paso a paso con Debug

# 12.6 Método MRO: Method Resolution Order

print(Cuadrado.mro())

