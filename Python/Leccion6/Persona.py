#CLASE 6: Tema Poo Parte 1(15/09)
class Persona: #Creamos una clase

    def __init__(self, nombre, apellido, edad):  # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Punto 8.8 Metodos de Instancia: Definimos un metodo
    def mostrar_detalle(self):
        print(f'Persona:{self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Ariel', 'Betancud', 40) # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
# Punto: 8.4-Tarea: Hacer el print igual que con el objeto 2
print(f"El objeto 1 de la clase Peronsa es: {persona1.nombre} {persona1.apellido} {persona1.edad}")

#Punto: 8.4 Creamos mas objetos en una clase
persona2 = Persona('Osvaldo', 'Giordanini', 45)
print(f"El objeto 2 de la clase Peronsa es: {persona2.nombre} {persona2.apellido} {persona2.edad}")


#Punto: 8.5 Referencia de moemoria objetos con debug
#Los objetos no comparten los valores, solo comparten los atributos.Asi se puede asignar
#Diferentes valores a cada atributo.


# Punto: 8.6 Modificar atributos de un objeto



#Punto 8.7: Metodos de instancia.Crear un UML.(Tarea diagramar )
# Los atributos son: caracteriscas

# Los atributos son: caracteriscas 

# Los métodos son: el comportamiento que van a tener los objetos (acciones)

#Punto 8.8 Metodos de Instancia: Definimos un método
persona1.mostrar_detalle()
persona2.mostrar_detalle()

