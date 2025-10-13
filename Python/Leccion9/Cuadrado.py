# 12.3 Creamos la clase hija Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'Cuadrado(ancho={self.ancho}, alto={self.alto}, area={self.calcular_area()}, color={self.color})'