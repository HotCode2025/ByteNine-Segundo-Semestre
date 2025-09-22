#CLASE 5-Tema: Funciones Recursivas Parte 3  -> Tarea(08-09)
#Punto: 7.6 Ejercicio 4 con funciones (impuestos)
#Ejercicio 4: Calculadora de Impuestos
#Crear una funcion para calcular el total de un pago incluyendo
#un impuesto aplicado(IVA)
#Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
#Proporcione el pago sin impuestos: 1000
#Proporcione el monto del impuesto: 21%
#Pago con impuesto: xxxxx
# Prueba de configuracion.

# Defino el porcentaje del IVA como una constante (21%)
IVA = 21
# Funcion que calcula el pago total incluyendo el impuesto IVA
def calcular_pago_con_impuesto(pago_sin_impuesto):
    # Formula: pago_sin_impuesto + (pago_sin_impuesto * porcentaje_IVA)
    # Ejemplo: 100 + (100 * 0.21) = 121
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (IVA /100) # Formmula
    return pago_total
# Solicitamos al usuario que ingrese el monto sin impuesto
pago = float(input("Digite su pago sin impuesto: "))
# Calculamos el total llamando a la funcion
total = calcular_pago_con_impuesto(pago)
# Mostramos el resultado
print(f"El pago con IVA({IVA}%): ${total:.2f}")

