#Ejercicio 4: Supongamos que se tiene un conjunto de calificaciones de un grupo de 10 alumnos
#Realizar un algoritmo para calcular la calificacion promedio y la más baja de todo el grupo
from functools import total_ordering

total = 0
menor = 99
for i in range (1, 11):
    notas = float (input(f"Ingrese nota {i}: "))
    total +=notas
    if notas < menor:
        menor = notas
promedio = total / 10
print(f"El promedio de las calificaciones ingresadas es: {promedio}")
print(f"La csalificacion más baja es: {menor}")
