#Para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye",}
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add(9) #No se pueden agregar varios elementos con el .add
print(conjunto1)
conjunto1.add("Hola")
print(3 not in conjunto1) #Preguntamos si el 3 no esta en el conjunto1

#Como hacer la igualdad de dos conjuntos
print(conjunto2 == conjunto1) 

#Operaciones de conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #Que elementos tienen en comun los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #Elementos que estan en el conjunto1 pero no en el conjunto2
print(conjunto3) #Asigna el valor que esta en conjunto1 pero no en conjunto2

conjunto3 = conjunto2 - conjunto1 #Elementos que estan en el conjunto2 pero no en el conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #Elementos que no se repiten en ambos conjuntos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) #Preguntamos si conjunto2 es un subconjunto de conjunto3
print(conjunto1.issubset(conjunto3)) #Preguntamos si conjunto1 es un subconjunto de conjunto3
print(conjunto3.issubset(conjunto2)) #Preguntamos si conjunto3 es un subconjunto de conjunto2
print(conjunto3.issubset(conjunto1)) #Preguntamos si conjunto3 es un subconjunto de conjunto1

print(conjunto3.issuperset(conjunto2)) #Preguntamos si conjunto3 es un superconjunto de conjunto2
print(conjunto3.issuperset(conjunto1)) #Preguntamos si conjunto3 es un superconjunto de conjunto1

print(conjunto2.issuperset(conjunto3)) #Preguntamos si conjunto2 es un superconjunto de conjunto3
print(conjunto1.issuperset(conjunto3)) #Preguntamos si conjunto1 es un superconjunto de conjunto3

#Como saber si hambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #Preguntamos si conjunto1 y conjunto2 son disconexos

#Convertir un conjunto totalmente inmutable
conjunto1 = frozenset # Esto hace que el conjunto1 sea inmutable
#No se puede agregar, modificar o eliminar elementos del conjunto 