# 12.2 Creamos las clases padres
class Color:
    def __init__(self, color):
        # asignamos directamente al atributo "privado"
        if not color:
            raise ValueError("El color no puede estar vacío")
        self._color = color

    # --- Propiedad ---
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nuevo_color):
        if not nuevo_color:
            raise ValueError("El color no puede estar vacío")
        self._color = nuevo_color

    def __str__(self):
        return f'Color [color: {self._color})'

