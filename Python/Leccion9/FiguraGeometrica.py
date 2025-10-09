# 12.2 Creamos las clase padres
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        # guardamos en atributos "privados"
        self._ancho = ancho
        self._alto = alto

    # --- Propiedades ---
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que cero")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que cero")
        self._alto = valor

    # --- Métodos ---
    def calcular_area(self):
        """Área genérica (ancho * alto). Puede sobrescribirse."""
        return self._ancho * self._alto

    def __str__(self):
        return f'FiguraGeometrica(ancho={self._ancho}, alto={self._alto})'

