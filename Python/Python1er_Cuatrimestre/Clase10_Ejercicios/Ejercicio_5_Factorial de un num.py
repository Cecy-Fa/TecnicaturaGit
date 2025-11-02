#Ejercicio 5: Calcular el factorial de un número mayor o igual a 0
import math
resultado = 0
num = int(input("Ingrese un número: "))
while num < 0:
    num = int(input("Ingrese un número: "))
else:
    resultado = math.factorial(num)
    print(f"El factorial de {num} es: {resultado}")