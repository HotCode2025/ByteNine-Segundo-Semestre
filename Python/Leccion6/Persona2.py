class Persona2:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property  #Decorador
    def nombre(self):  #Metodo Getter
        print("Estamos utilizando el metodo Getter")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  #Metodo Setter
        print("Estamos utilizando el metodo Setter")
        self._nombre = nombre

    @property
    def apellido(self):
        print("Estamos utilizando el metodo Getter")
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print("Estamos utilizando el metodo Setter")
        self._apellido = apellido

    @property
    def edad(self):
        print("Estamos utilizando el metodo Getter")
        return self._edad

    @edad.setter
    def edad(self, edad):
        print("Estamos utilizando el metodo Setter")
        self._edad= edad

if __name__ == '__main__':
    persona1 = Persona2("Ariel", "Bentancud", "41")
    #Llamamos al metodo Getter
    print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)

    persona1.nombre = "Juan Pedro"  #Llamamos al metodo Setter
    print(persona1.nombre) #Nuevamente con el metodo Getter
    print(persona1.mostrar_detalles()) #Llamamos al metodo mostrar_detalles

    # Atributo read-only (solo lectura) seria la edad porque no tiene el metodo set
    print(persona1.edad)

    print(__name__)