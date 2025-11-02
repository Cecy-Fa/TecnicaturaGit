#Ejercicio 1: Año Bisiesto
#Diseñar un programa que ingresando un año, nos devuelva por consola
#si es un año bisiesto o no, repetir la acción del usuario lo desida.

print("Comprobamos que año es Bisiesto")
while True:
    num = int(input("Ingrese el año: "))
    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        print(f"El año {num} es bisiesto")
    else:
        print(f"El año {num} No es bisiesto")
    opcion = int(input("Para seguir ingrese 1, para salir ingrese cualquier número: "))
    if opcion != 1:
        break