"""Ejercicio 1:
1_Solicite al usuario que ingrese un numero
2_Este se asigna una variable
3_Utilizaremos la estructura "if ele"
4_la formula:<num>%2==0 esta operacion
nos dice si es un numero par
5_Si es True imprimimos que es par
6_Si es False imprimimos que es impar
"""
from selectors import SelectSelector

a = int(input("Digite un numero: "))
print(f"El residuo de la división es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de la a es: {a} es un numero PAR")
else:
    print(f"El valor de la a es: {a} es un numero IMPAR")