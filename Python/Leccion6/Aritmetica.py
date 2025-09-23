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


Aritmetica1 = Aritmetica(5, 3)  # le pasamos los argumentos para los operandos
print(Aritmetica1.sumar())
