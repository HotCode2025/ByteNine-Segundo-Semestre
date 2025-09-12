#Comenzamos con Funciones
#mi_funcion() # No se puede llamar antes de definir a una funcion
#Definimos una funcion
def mi_funcion(): #Para identificar la funcion utilizamos parentesis
    print('Saludos a todos los alumnos de la Tecnicatura')
mi_funcion() #Estamos llamando a la funcion
mi_funcion() #Se puede llamr a una funcion N cantidad de veces

#CLASE 5-Tema: Funciones Parte 2 -> Tarea(08-09)
#punto: 6.3 List Unpacking: Desempaquetado de listas
def show(name, lastName):
    print(name+' '+lastName)
person =["Ariel", "Betancud"]
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") # Desempaquetamos a traves de una tupla
show(*person2)
person3 ={"lastName": "Lucero", "name": "Natalia"}
show(**person3)

##punto:6.4 Repaso del Ciclo for else
numbers = [1, 2, 3, 4, 5] # Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no see ejecute el else
else:
    print('Esto se termino')

#Punto:6.5 List Comprehension: Lista de Comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

#Punto: 6.6 Funciones: Paso de Argumentos
def mi_funcion2(name, lastname):
    print("Saludos a todos los que ven a traves del canal de Youtube")
    print(f'Nombre: {name}, Apellido: {lastname}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

#Punto: 6.7 Funciones: Palabra return
#Creamos una funcion para sumar
def sumar(a, b):
    return a + b
#resultado = sumar (78, 22)
#print(f'El resultado de la suma es: {resultado}')
print (f'El resultado de la suma es: {sumar(55, 45)}')

#Punto: 6.8 Funciones: Valores por Default en Argumentos
def sumar2(a = 0, b = 0):# Le ddamos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}') #Muestra valor por default
print(f'Resultado de la suma: {sumar2(22, 66)}')# Muestra  los resultados

#Punto: 6.9 Funciones: Argumentos, Variables en Funciones
def listarNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in  nombres: # Se va a convertir en una Tupla
        print((nombre))
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcelo', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

#CLASE 5-Tema: Funciones Recursivas Parte 3  -> Tarea(08-09)
#Punto: 7.2 Argumentos variables para un diccionario
def listarTerminos(**terminos): # lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # Kwargs significa: Key word argument
        print(f'{llave} : {valor}')
listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE= 'Integrated Develoment Enviroment', PK= 'Primary Key')
listarTerminos(Nombre= 'Leonel Messi')

##Punto: 7.3 Lista de elementos con funciones (convertir)
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10, 11) No es un objeto iterable
desplegarNombres((10, 11))# La convertimos a una tupla para recorrerla.En un solo elemneto no olvidar la coma
desplegarNombres([22, 55])# convertimos la funcion en una lista para recorrerla

#Punto: 7.4 Funciones recursivas con factorial (hacer la tarea)
def factorial(numero):
    if numero == 1: #Caso base
        return 1
    else:
        return  numero * factorial(numero-1)#Caso recursivo

resultado = factorial(5)# Lo hacemos en codigo duro
print(f'el factorial del numero 5 es: {resultado}')

#Tarea que el usuario ingrese el numero para calcular el Factorial


