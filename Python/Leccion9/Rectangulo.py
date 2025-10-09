# Tarea 12.7 creación Rectangulo
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.ancho * self.alto

    def __str__(self):
        return (f'Rectangulo(ancho={self.ancho}, alto={self.alto}, '
                f'area={self.calcular_area()}, color={self.color})')

