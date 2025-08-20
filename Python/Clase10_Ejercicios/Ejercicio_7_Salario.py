#Ejercicio 7:
# #Dadas las horas trabajadas de 5 personas y
# #la tarifa de pago.
#Calcular el salario, y la sumatoria de todos
#los salarios.

i = 1
suma = 0

while i <= 5:
    print(f"Ingrese el salario del empleado {i}")
    horas = float(input("Ingrese las horas de trabajo: "))
    tarifa = float(input("Ingrese la tarifa por hora: "))
    salario = horas * tarifa
    print(f"El salario del empleado es: {salario}")
    suma += salario
    i += 1

#Mostramos suma de los salarios
print(f"La suma de los salarios es: {suma}")
