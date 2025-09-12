#Clase 1(11/08)Teoria Practica Colecciones(listas-Tupla)
#lista = Ariel, Liliana, Natalia, Osvaldo
#COLECCIONES EN PYTHON
#COLECCION LISTAS(arreglos o vectores)

nombres = ['Naty','Osvaldo', 'Lily','Ariel']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

#Recuperar un rango de la lista
print(nombres[0:2])#Solo muestra el indice 0, 1 pero no el indice 2
#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])#indices a mostrar 0, 1, 2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres))#le pasamos como parametro la lista

#Agregar un elemento
nombres.append('Marcelo')
print(nombres)
#CLASE2.repaso.Diferentes tipos de datos
nombres.append([1,2,3])#lista dentro de una lista
nombres.append(True)#Tipo booleano
nombres.append(10.45)#Tipo float
nombres.append([4,5])
nombres.append(7)
print(nombres)
#Fin repaso

#Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)
#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)
#Eliminamos el ultimo elemento
nombres.pop()
print(nombres)
#Eliminamos un indice especifico
del nombres[2]#del significa delete(eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
#del nombres
#print(nombres)#Va a marcar error porque la lista se borro

#COLECCION TUPLA
#Definimos una TUPLA
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print (len(cocina))

# Acceder a un elemento.Para este utilizamos corchetes"No" parentesis
print(cocina[0])
# mostrar de manera inversa(ultimo elemento)
print(cocina[-1])

# Acceder a un rango(mostrar mas elementos)
print(cocina[0:2])

#Ejemplo de NO TUPLA
verduras = ('papa')
print(verduras)
verdura =('papa', )#para que sea una tupla, necesita aunque sea un solo elemnto la "coma"
#De lo contrario seria un tipo string cadena.
print(verdura)
print(verdura[0])

#Recorremos los elementos de una tupla
for cocinar in cocina:
    #print(cocinar) me lo va a mostrar en columna.# Print esta usando  \n para saltos de linea
    print(cocinar, end= ' ')#Usamos end = para eliminar los saltos de linea
# Con esta manera eliminamos el end
##Modificar tupla(conversion). En la buena práctica NO es recomendable
cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print("\n", cocina)

#Eliminar tupla
## del cocina Esto es para eliminar tupla
print(cocina)

# CLASE 2: 18-08
#COLECCIONES EN PYTHON
#COLECCION  SET
#Tipo set(conjunto)
planetas = {'Marte','Júpiter', 'Venus'}
print(len(planetas))#Usamos la FUNCI0N len = length significa largo

# Revisar si un elemento existe dentro de set.Respeta mayus,minus y acentos
print('Jupiper' in planetas)#Devuelve un booleano.¿Esta Júpiter en planetas?
print('Jupiper'  not in planetas)#Devuelve un booleano.¿Júpiter no esta en planetas?

# Agregar un elemento. No se pueden agregar elementos duplicados o repetidos
planetas.add('Tierra')#FUNCION add
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe.
planetas.remove('Júpiter')# FUNCION remove. Ante un mal ingreso u inexistencia da ERROR
print(planetas)
planetas.discard('tierra')#FUNCION discard.No da ERROR, pero no borra el elemento
print(planetas)

# Limpiar set
planetas.clear()#FUNCION clear. Limpia el conjunto(<vacio)
print(planetas)

#Eliminar set
#del planetas #Borra el conjunto y dara error
#print(planetas)

# DICCIONARIO EN PYTHON
#'Maradona: 10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
#dict(key,value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
#Verificar la cantidad de elementos de un diccionario
print(diccionario)
print(len(diccionario))#FUNCION len

#Acceder a un diccionario con la llave(key)
print(diccionario ['IDE'])#Datos a ingresar precisos, de lo contrario ERROR

#otra forma de recuperar un elemento(acceder)
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos los elementos.
diccionario['IDE']= 'Entorno de Desarrollo Integrado'
print(diccionario)

#Como recorre los elementos con FOR
for termino in diccionario:
    print(termino)# Recorrer y mostrar solo llave

#Necesitamos una FUNCION para recorrer un diccionario.FUNCION: ( .items())
for termino, valor in diccionario.items():
    print(termino, valor)#Recorrer mostrando llave y valor


#otras maneras de acceder a un diccionario.Individualmente
# FUNCION .key()
for termino in diccionario.keys():
    print(termino)#Muestra solo las llaves
# FUNCION .values()
for valor  in diccionario.values():
    print(valor)#Muestra solo los valores

#Comprobar la existencia de algún elemento.Valor Booleano
print('IDE' in diccionario)#Devuelve un booleano.¿Esta IDE en diccionario?
print('IDE' not in diccionario)#Devuelve un booleano.¿ IDE no esta en diccionario?

# Agreagar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar elemento. funcion .pop('Key')
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario. FUNCION .cleaar()
diccionario.clear()
print(diccionario)

#Eliminar diccionario
#del diccionario#Se borra el diccionario
#print(diccionario)

#REPASO Y CONCEPTOS DE LISTAS
#Concatenamos Listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2#Concatenacion
print(lista3)

#FUNCION .extend
lista3.extend([7, 8, 9, 1])#Agrega varios elementos a la lista
print(lista3)

#FUNCION: .index
print(lista3.index(5))#Para saber la posición del valor ingresado
#print(lista3.index(0))#Error si no es elemento de lista.

#Valores repetidos en una lista
print(lista3.count(1))#Cuenta cuantos valores iguales hay

#Poner lista al reves
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo los elementos.REPETIR
lista = [1,2,3] * 2
print(lista)
lista = lista3 * 2
print(lista)

#Metodos de  Ordenamiento(Ascendente/descendente)
lista3.sort()
print(lista3)#Ascendente
lista3.sort(reverse = True)
print(lista3)#Descendente

#REPASO Y MAS CONCEPTOS DE TUPLAS
#Tipo de datos
tupla = (4,'Hola', 6.78,[1, 2, 3], 4, 4, 'Hola')#puede tener diferentes tipos de datos dentro
print(tupla)

#Buscar elemento en tupla
print(4 in tupla)#Devuelve booleano.¿Esta el elemento 4 en tupla?
print(4 not in tupla)#Devuelve booleano. ¿4 no esta en tupla?

#Lo que podemos usar dentro de TUPLAS: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# CLASE 3(25-08)
#3.1-Repaso del tipo SET o Conjunto
#Para definir un conjunto(set)
conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1)#¿El numero 3 NO ESTA EN EL CONJUNTO1?

#Como hacer la igualdad de 2 conjuntos
print(conjunto1 == conjunto2)#Nos devuelve como respuesta un booleano

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #Union.La linea es la que une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #Interseccion.Elementos que tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2#Diferencia.Asigna el valor que esta en el conjunto1 y no esta en conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2#Diferencia Simetrica.Elementos que no corparten o que son diferentes entre ambos.
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) #Subconjuntos. Preguntar si un conjunto es un subconjunto dentro de otro.
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issubset(conjunto3)) # preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issubset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es u superconjunto
print(conjunto2.issubset(conjunto3))

#Como ssaber si ambos conjuntos son disconexos, esto  es si no comparten elementos en comun.
print(conjunto1.isdisjoint(conjunto2))#Preguntamos si existen cosas en comun

#Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# 3.2-Repaso Diccionarios
diccionarioNuevo = {'Azul' : 'Blue', 'Rojo' :'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#3.3 Ejercicio con Diccionario y Tarea
# Los diccionarios pueden almacenar diferentes  tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

#3.3-Diccionario y Tarea
#Diccionario Seleccion Argentina
seleccionArgentina = {
    10 : {'Nombre': 'Lionel Mesi', 'Edad': 35, 'Altura': 1.70, 'Precio': ' 50 millones', 'Posicion': 'Extremo Derecho'},
    11 : {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.83, 'Precio': '12 millones', 'Posicion': 'Extremo Derecho'},
    24 : {'Nombre': 'Paulo Dvbala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media Punta'},
    19 : {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa Central'},
     1 : {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
}
print(seleccionArgentina.values())

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Tenemos cargados en el diccionario la cantidad de jugadores: ',end = ' ')
print(len(seleccionArgentina))

#Tarea ingresar 3 a 4 Jugadores mas.
print("--------ACTUALIZACION DICCIONARIO----------")

seleccionArgentina = {
    10 : {'Nombre': 'Lionel Mesi', 'Edad': 35, 'Altura': 1.70, 'Precio': ' 50 millones', 'Posicion': 'Extremo Derecho'},
    11 : {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.83, 'Precio': '12 millones', 'Posicion': 'Extremo Derecho'},
    21 : {'Nombre': 'Paulo Dvbala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media Punta'},
    19 :{'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa Central'},
     1 :{'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
}
del seleccionArgentina[11] # Elimino a Agel Di Maria
del seleccionArgentina[21] # Elimino a Paulo Dvbala
del seleccionArgentina[1]  # Elimina a Franco Armani


seleccionArgentina[24] = {'Nombre': 'Nahuel Molina', "Edad": 27, "Altura": 1.75, "Precio": "20 Millones", "Posicion": "Lateral Derecho"}
seleccionArgentina[22] = {"Nombre": "Lautaro Martinez", "Edad": 27, "Altura": 1.74, "Precio": "95 Millones", "Posicion": "Delantero"}
seleccionArgentina[23] = {"Nombre": "Lisandro Martinez", "Edad": 26, "Altura": 1.75, "Precio": "50 Millones", "Posicion": "Defensa Central"}
seleccionArgentina[20] = {"Nombre": "Alexis Mac Allister", "Edad": 25, "Altura": 1.76, "Precio": "100 Millones", "Posicion": "Mediocampista"}
seleccionArgentina[9] =  {"Nombre": "Julian Alvarez", "Edad": 24, "Altura": 1.70, "Precio": "100 Millones", "Posicion": "Delantero"}
seleccionArgentina[8] =  {"Nombre": "Marcos Javier Acuña", "Edad": 33, "Altura": 1.72, "Precio": "2 Millones", "Posicion": "Lateral izquierdo"}
seleccionArgentina[5] =  {"Nombre": "Leandro Paredes", "Edad": 31, "Altura": 1.80, "Precio": "5 Millones", "Posicion": "Pivote"}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print(f"Total de jugadores cargados: {len(seleccionArgentina)}")


#3.4-Metodo con Litas llamado PILAS
pila = [1, 2, 3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop()# Quita el ultimo elemento y lo guarda en la variable.
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

#3.5-Metodo con LISTAS llamado COLA
#Colas con listas
#Estructura de datos de tipo fifo(first input / first output
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)


#CLASE 4-Tema: Ejercicios y Más -> Tarea(01-09)
#Punto: 4.5 Recorremos el Diccionario seleccionArgentina
#Otra forma de mostrar un diccionario
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')

