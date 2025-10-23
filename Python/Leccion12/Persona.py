# 15.6 Sobrecarga de Operadores: Parte 2a
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other): # Other significa = otro
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, otro):
        return self.edad - otro.edad  #15.7 Sobrecarga de Operadores: Parte 2b

persona1 = Persona('Ariel', 40)
persona2 = Persona('Betancud', 5)

# persona1.__add__(persona2) sintaxis interna y automática

print(persona1 + persona2)
print(persona1 - persona2) # 15.7 Sobrecarga de Operadores: Parte 2b
