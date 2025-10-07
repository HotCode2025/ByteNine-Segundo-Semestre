# Clase padre
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}"


# Clase hija Auto
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad  # km/hr

    def __str__(self):
        return f"{super().__str__()}, Velocidad: {self.velocidad} km/hr"


# Clase hija Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo  # urbana, montaña, etc.

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"


# Creamos un objeto de cada clase
vehiculo = Vehiculo("Rojo", 4)
auto = Auto("Azul", 4, 180)
bicicleta = Bicicleta("Verde", 2, "Montaña")

# Mostramos los objetos
print("Vehículo:", vehiculo)
print("Auto:", auto)
print("Bicicleta:", bicicleta)