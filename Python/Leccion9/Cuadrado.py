# 12.3 Creamos la clase hija Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # inicializamos ambas superclases explícitamente
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.ancho * self.alto

    def __str__(self):
        return (f'Cuadrado(lado={self.ancho}, '
                f'area={self.calcular_area()}, '
                f'color={self.color})')
