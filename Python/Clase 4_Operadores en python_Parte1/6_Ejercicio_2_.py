"""Ejercicio 2:
1_Pedir un numero al usuario
2_Almacenar el valor en una variable
3_Usar la estructura "if else"
4_La formula es: <num> >=18
5_True: Eres mayor de edad, imprimir
6_False: Eres menor de edad, imprimir
"""
edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, usted es menor de edad")