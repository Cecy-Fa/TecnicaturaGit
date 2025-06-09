"""
Escribir la siguiente expresion
en forma de expresión algorítmica.
(a*3 * (b * 2 -2 * a * c)) / (2 * b)
1_Pedimos al usuario 3 valores = a,B,c
2_Mostramos el resultado final
"""
#Peso 1: Pedimos al usuario los valores
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

#Calculamos la expresión
resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)

#Paso 3: Mostramos el resultado final
print("El resultado es : ",resultado)