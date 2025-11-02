#Ejericico04: Calculadora de Impuestos
#(Clase 5 FUNCIONES RECURSIVAS 3ra Parte video 6 Py)
#Crear una función para calcular el total de un pago incluyendo
#un impuesto aplicado. (IVA)
#Formula: pagototal = pago_sin_impuesto + pago_sin:impuesto * (impuesto/100)
#Proporcione el pago sin impuesto: 1000
#proporcione el monto del impuesto: 21%
#pago con impuesto: xxxxxx

#Creamos la función que calcula el total del pago incluyendo el impuesto
def calcular_total(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

#Ejecutamos la función
pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: ")) #Variable descrptiva
impuesto = float(input("Proporcione el monto del impuesto (%): "))
pago_final = calcular_total(pago_sin_impuesto, impuesto)

print(f"Pago con impuesto: {pago_final}")
