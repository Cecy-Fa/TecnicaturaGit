"""Ejercicio1:
1_Pedimos al usuario un valor numerico
2_Verificar si el valor ingresado se encuentra
entre el rango de 0 a 5
3_La formula es: <num> >=0 and <num> <=5
"""
valor = int(input("Digite un numero dentro del rango 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
   print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} NO esta dentro del rango")

