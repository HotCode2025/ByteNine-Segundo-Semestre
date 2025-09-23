#Clase 7 POO Parte 2 Tarea (22/09)
class Aritmetica:
    """
    este tipo de comentario se llama docstring
    y sirve para documentar la clase
    vamos a hacer algunas opreraciones de suma, resta, multiplicacion y division
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # metodo de suma
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

Aritmetica1 = Aritmetica(5, 3)  # le pasamos los argumentos para los operandos
print(f'La suma de los números es: {Aritmetica1.sumar()}')
print(f'La resta de los números es: {Aritmetica1.resta()}')
print(f'La multiplicación de los números es: {Aritmetica1.multiplicar()}')
print(f'La división de los números es: {Aritmetica1.dividir():.2f}')
