# 15.6 Sobrecarga de Operadores: Parte 2a
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other): # Other significa = otro
        return f'{self.nombre} {other.nombre}'

persona1 = Persona('Ariel', 40)
persona2 = Persona('Betancud', 5)

# persona1.__add__(persona2) sintaxis interna y automática

print(persona1 + persona2)



