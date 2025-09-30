from Persona2 import Persona2
print('Creacion de objetos'.center(50, '-')) #Punto 10.6
if __name__ == '__main__':
    persona5 = Persona2('Lionel', 'Messi', 35)
    persona5.mostrar_detalles()

    print(__name__)

#Clase 8:POO Parte 3Metodos set& get Tarea
#Punto 10.6 Destructor de objetos
print('Eliminacion de Objetos'.center(50, '-'))
del persona5 #No es muy comun