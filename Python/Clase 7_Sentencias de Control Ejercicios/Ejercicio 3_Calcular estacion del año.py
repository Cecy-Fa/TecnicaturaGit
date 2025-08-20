'''Ejercicio 3: Calcular la estacion del año
#Verano: 21/12 al 21/03 -> 1,2,3
#otoño: 21/03 al 21/06 -> 4,5,6
#Invierno: 21/06 al 21/09 -> 7,8,9
#Primavera: 21/09 al 21/12 -> 10,,11,12
'''
mes = int(input("Ingrese el mes (1-12):"))
if mes == 1 or mes == 2 or mes == 3:
    print("Verano")
elif mes == 4 or mes == 5 or mes == 6:
    print("Otoño")
elif mes == 7 or mes == 8 or mes == 9:
    print("Invierno")
elif mes == 10 or mes == 11 or mes == 12:
    print("Primavera")
else:
    print("Mes no valido. Debe ser un número entre 1 y 12")
