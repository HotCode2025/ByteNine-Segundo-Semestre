class Rectangulo:
    def __init__(self):
        self.Altura = float(input("Ingrese la altura del rectangulo\n"))
        self.Base = float(input("Ingrese la base del rectangulo\n"))

    def calcular_area(self ):
        return self.Altura * self.Base


rectangulo1 = Rectangulo()
rectangulo2 = Rectangulo()
rectangulo3 = Rectangulo()

print(f"Area rectangulo 1°: {rectangulo1.calcular_area()}")
print(f"Area rectangulo 2°: {rectangulo2.calcular_area()}")
print(f"Area rectangulo 3°: {rectangulo3.calcular_area()}")