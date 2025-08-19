planetas = {"Marte","Jupiter","Saturno","Venus","Tierra"}

print(len(planetas))

#Revisar si un elemento existe dentro el set

print("Marte" in planetas)

#Agregar un elemento al set
planetas.add("Mercurio")

print(planetas)

print(len(planetas))

#Eliminar un elemento del set, puede arrojar un error si el elemento no existe

planetas.remove("Venus") #Esta función lanza un error si el elemento no existe

print(planetas)

planetas.discard("Tierra") #Esta función no lanza un error si el elemento no existe

print(planetas)

#Limpiar el set
planetas.clear()

print(planetas)

# Eliminar el set

del planetas

print(planetas)  # Esto generará un error porque 'planetas' ya no existe