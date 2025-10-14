# Clase 9 POO Parte 5 Herencia Múltiple Tarea
# 12.4 Creamos la clase para testear nuestro código
from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creación de objetos clase Cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(8, 'Azul')
cuadrado1.alto = 7
#cuadrado1.ancho = 7 #Comentado en 13.5 (si modificamos un valor debemos quitar todos los set para ponerlo como atributo de solo lectura)
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
print(f'Calculo del área del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
# print(Cuadrado.mro())

print(cuadrado1)
print('Creacion de objeto clase Rectangulo'.center(50, '_')) # 12.7 Tarea Ejercicio Rectangulo
rectangulo1 = Rectangulo(3, 9, 'verde')
rectangulo1.ancho = 8
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#figura1 = FiguraGeometrica()#No se puede instanciar, es abstracta #13.4 clase abstracta
print(Cuadrado.mro())