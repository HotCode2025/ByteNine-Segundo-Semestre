#La tarea consiste en ingresar elementos al diccionario llamado seleccionArgentina,lo elementos a ingresar deben ser como mínimo 4, 
# estos elementos son los jugadores con su número de camiseta, nombre, apellido, edad, altura, precio y posición de juego, 
# por supuesto ver el video anterior.

seleccionArgentina = {
    10: {"Nombre":"Lionel Messi", "Edad":36, "Altura":1.70, "Precio":18000000, "Posición":"Delantero"},
    9: {"Nombre":"Julian Alvarez", "Edad":23, "Altura":1.70, "Precio":100000000, "Posición":"Delantero"},
    23: {"Nombre":"Emiliano Martinez", "Edad":31, "Altura":1.95, "Precio":20000000, "Posición":"Arquero"},
    24: {"Nombre":"Enzo Fernandez", "Edad":24, "Altura":1.78, "Precio":50000000, "Posición":"Mediocampista"},
    13: {'Nombre': 'Cristian Romero', 'Edad': 26, 'Altura': 1.85, 'Precio':60000000, 'Posicion': 'Defensor Central'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 36, 'Altura': 1.83, 'Precio':3000000, 'Posicion': 'Defensor Central'},
    3: {'Nombre': 'Nicolás Tagliafico', 'Edad': 31, 'Altura': 1.72, 'Precio':15000000, 'Posicion': 'Lateral Izquierdo'},
    26: {'Nombre': 'Nahuel Molina', 'Edad': 26, 'Altura': 1.75, 'Precio':40000000, 'Posicion': 'Lateral Derecho'},
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print(len(seleccionArgentina))
