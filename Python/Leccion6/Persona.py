 #CLASE 6: Tema Poo Parte 1(15/09) Gustavo
class Persona: #Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.wkargs = kwargs

        # Getters
        @property
        def nombre(self):
            return self._nombre

        @property
        def apellido(self):
            return self._apellido

        @property
        def dni(self):
            return self._dni

        @property
        def edad(self):
            return self._edad

        # Setters
        @nombre.setter
        def nombre(self, nuevo_nombre):
            self._nombre = nuevo_nombre

        @apellido.setter
        def apellido(self, nuevo_apellido):
            self._apellido = nuevo_apellido

        @dni.setter
        def dni(self, nuevo_dni):
            self._dni = nuevo_dni

        @edad.setter
        def edad(self, nueva_edad):
            self._edad = nueva_edad

# Punto 8.8 Metodos de Instancia: Definimos un metodo

    def mostrar_detalle(self): # Self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.wkargs}')


persona1 = Persona('Ariel', 'Betancud', 32455987, 40) # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
# Punto: 8.4-Tarea: Hacer el print igual que con el objeto 2


#Punto: 8.4 Creamos mas objetos en una clase
print(f"El objeto 1  de la clase Peronsa es: {persona1.nombre} {persona1.apellido} {persona1.edad}")
persona2 = Persona('Osvaldo', 'Giordanini', 30321456, 45)
print(f"El objeto 2 de la clase Peronsa es: {persona2.nombre} {persona2.apellido} {persona2.edad}")


#Punto: 8.5 Referencia de moemoria objetos con debug
#Los objetos no comparten los valores, solo comparten los atributos.Asi se puede asignar
#Diferentes valores a cada atributo.


# Punto: 8.6 Modificar atributos de un objeto
persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto 1 modificado de la clase Persona es: {persona1.nombre} {persona1.apellido} {persona1.edad}")


#Punto 8.7: Metodos de instancia.Crear un UML.(Tarea diagramar )
# Los atributos son: caracteriscas

# Los atributos son: caracteriscas 

# Los métodos son: el comportamiento que van a tener los objetos (acciones)


#Punto 8.8 Metodos de Instancia: Definimos un método.
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Punto 9.1 Palabra reservada self y atributos de instancia
Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dará error

# Punto 9.2 Crear Atributos desde  un Objeto
persona1.telefono = "44445555289"
print(f"Este es el telefono:{persona1.nombre} {persona1.telefono}") # Hemos creado unb atributo de un objeto

# print(persona2.telefono)el objecto persona2 no tiene este atributo, da error

# 9.7 Metodo init Dunder con argumentos variables
persona3 = Persona("Rogelio","Romero", 35789456, 22, "Telefono","2664761270", "Calle Lopes","4283","Manzana", 77, "Casa", 18, Altura=1.83, Peso=105, CFavorito="Amarillo", Auto="Fiat", Modelo=2012)
persona3.mostrar_detalle()
# print(persona3._dni) # Esto no se debe utilizar (esta encapsulado), esto dice que lo desconocemos python
# persona3.__nombre # Esta totalmente encapsulado

# Tarea 10.3

# Creamos tres objetos más
persona4 = Persona("María", "Pérez", 40256789, 30)
persona5 = Persona("Juan", "López", 39234567, 28)
persona6 = Persona("Carla", "Fernández", 41234567, 35)

# Mostramos detalles originales
print("\n--- Antes de modificaciones ---")
persona4.mostrar_detalle()
persona5.mostrar_detalle()
persona6.mostrar_detalle()

# Modificamos con setters
persona4.nombre = "Mariana"
persona5.apellido = "Gómez"
persona6.edad = 36

# Mostramos detalles modificados
print("\n--- Después de modificaciones ---")
persona4.mostrar_detalle()
persona5.mostrar_detalle()
persona6.mostrar_detalle()
