class Cubo:
    """
    Clase 7: Tema Poo Parte 2-Tarea(22-09)
    Crear la clase Cubo con los atributos, ancho, alto y profundidad,
    con un metpdo calcular_volumen que tendrá la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores
    """

    def __init__(self, ancho, alto, profundidad):
        """
        Metodo constructor(inicializamos los atributos del cubo
        """
        self.ancho = ancho  # Lo digita el usuario
        self.alto = alto  # Asignacion, lo digita el usuario
        self.profundidad = profundidad  # la digita el usuario

    def calcular_volumen(self):
        """
        Metodo para calcular el volumen
        """
        return self.ancho * self.alto * self.profundidad

# Pedir al usuario que digito los valores del cubo
ancho_digitado = float(input("Digite el ancho del cubo: "))
alto_digitado = float(input(" Digite el alto del cubo: "))
profundidad_digitada = float(input("Digite la profundidad del cubo: "))

# Instancia del objeto de la clase CUbo
el_cubo = Cubo(ancho_digitado, alto_digitado, profundidad_digitada)

# Llamamos el metodo calcular_volumen
volumen = el_cubo.calcular_volumen()

# Mostrar resultados
print(f"El volumen del cubo es: {volumen}")
