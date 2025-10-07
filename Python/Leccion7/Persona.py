# Tarea: encapsular los atributos y agregar los métodos getter and setters
# Crear otros objetos, pasar los datos para nombre. edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente
# Clase 9 - 11.3 Herencia  11.4 Tarea

class Persona: # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre # Atributos
        self._edad= edad

    # Getters
    def get_nombre(self):
        return self._nombre
    def get_edad(self):
        return self._edad

    # Setters
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0: # Realizamos una validación para la edad
            self._edad = nueva_edad
        else: print("La edad no puede ser negativa. ")

class Empleado(Persona): # Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre,edad)
        self._sueldo = sueldo

    # Getter
    def get_sueldo(self):
        return self._sueldo

    # Setter
    def set_sueldo(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self._sueldo = nuevo_sueldo
        else:
            print("El sueldo no puede ser negativo. ")

# Creamos los objetos

empleado1 = Empleado('Ariel', 40, 75000)
empleado2 = Empleado("Marcos", 32, 85000)

# print(empleado1.nombre)
# print(empleado1.edad)
# print(empleado1.sueldo)

# Mostramos los datos originales
print("=== Datos Originales ===")
print("Empleado 1: ",empleado1.get_nombre(), empleado1.get_edad(), empleado1.get_sueldo())
print("Empleado 2: ",empleado2.get_nombre(), empleado2.get_edad(), empleado2.get_sueldo())

# Modificamos los valores con setters
empleado1.set_nombre("Ariel Betancud")
empleado1.set_edad(41)
empleado1.set_sueldo(85000)

empleado2.set_nombre("Marcos Martinez")
empleado2.set_edad(33)
empleado2.set_sueldo(95000)

# Mostramos los datos modificados
print("\n=== Datos modificados ===")
print("Empleado 1:",empleado1.get_nombre(),empleado1.get_edad(),empleado1.get_sueldo())
print("Empleado 2:",empleado2.get_nombre(),empleado2.get_edad(),empleado2.get_sueldo())





