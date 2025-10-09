# Clase 9 POO Parte 5 Herencia Múltiple Tarea
# 12.4 Creamos la clase para testear nuestro código

from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

def main():
    print('=== PRUEBAS DE FIGURAS GEOMÉTRICAS ===')

    # Creamos los objetos
    cuadrado1 = Cuadrado(5, 'Azul')
    cuadrado2 = Cuadrado(3, 'Rojo')

    # 12.7 Tarea Ejercicio Rectangulo
    rect1 = Rectangulo(4, 6, 'Verde')
    rect2 = Rectangulo(10, 2, 'Amarillo')

    figuras = [cuadrado1, cuadrado2, rect1, rect2]

    # Mostramos los resultados
    for figura in figuras:
        print(figura)  # usa __str__ correcto de cada clase
        print(f"Área calculada: {figura.calcular_area()}")
        print('-' * 40)

    # Modificamos de Atributos
    print("\n=== MODIFICACIÓN DE ATRIBUTOS CON PROPERTY ===")
    cuadrado1.color = 'Celeste'
    cuadrado1.ancho = 8
    cuadrado1.alto = 8
    print(cuadrado1)

    # 12.6 Método MRO: Method Resolution Order
    print("\nMRO de Cuadrado:", Cuadrado.mro())
    print("\nMRO de Rectangulo:", Rectangulo.mro())


if __name__ == '__main__':
    main()


