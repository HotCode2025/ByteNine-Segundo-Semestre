 #CLASE 6: Tema Poo Parte 1(15/09) Gustavo
class Persona: #Creamos una clase

    def __init__(self, nombre, apellido, edad, *args, **kwargs):  # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.wkargs = kwargs

# Punto 8.8 Metodos de Instancia: Definimos un metodo

    def mostrar_detalle(self): # Self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad}, la direccion es: {self.args}, los adtos importantes son: {self.wkargs}')


persona1 = Persona('Ariel', 'Betancud', 40) # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
# Punto: 8.4-Tarea: Hacer el print igual que con el objeto 2


#Punto: 8.4 Creamos mas objetos en una clase
print(f"El objeto 1  de la clase Peronsa es: {persona1.nombre} {persona1.apellido} {persona1.edad}")
persona2 = Persona('Osvaldo', 'Giordanini', 45)
print(f"El objeto 2 de la clase Peronsa es: {persona2.nombre} {persona2.apellido} {persona2.edad}")


#Punto: 8.5 Referencia de moemoria objetos con debug
#Los objetos no comparten los valores, solo comparten los atributos.Asi se puede asignar
#Diferentes valores a cada atributo.


# Punto: 8.6 Modificar atributos de un objeto
persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto 1 modificado de la clase Peronsa es: {persona1.nombre} {persona1.apellido} {persona1.edad}")


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
persona3 = Persona("Rogelio","Romero", 22, "Telefono","2664761270", "Calle Lopes","4283","Manzana", 77, "Casa", 18, Altura=1.83, Peso=105, CFavorito="Amarillo", Auto="Fiat", Modelo=2012)
persona3.mostrar_detalle()