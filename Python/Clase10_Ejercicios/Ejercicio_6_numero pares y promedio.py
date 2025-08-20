#Ejercicio 5: Ingresar "N" numeros enteros, visualizar la suma de los
#números pares de la lista, cuántos números pares existen y cuál
# es el promedio de los números
n = int(input("Ingrese cuantos numeros desea calcular: "))
num_impar = 0
num_par = 0
suma_impar = 0
suma_par = 0

while n > 0:
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        num_par += 1
        suma_par += num
    else:
        num_impar += 1
        suma_impar += num
    n -= 1
#Mostramos la suma de los numeros pares
print(f"La suma de los numeros pares es: {suma_par}")
#Mostramos la cantidad de los numeros pares
print(f"La cantidad de los numeros pares es: {num_par}")
#Mostramos el promedio de los numeros impares
if num_impar > 0:
    print(f"El calculo del promedio de los numeros impares es:  {suma_impar / num_impar}")
else:
    print("No se ingresaron numeros impares")
