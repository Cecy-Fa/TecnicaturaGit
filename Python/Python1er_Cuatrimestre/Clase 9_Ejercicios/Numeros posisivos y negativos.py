#Ejercicio 3: Leer 10 números e imprimir cuántos son:
#positivos y negativos

conteo_positivo = 0
conteo_negativo = 0
conteo_neutro = 0

for i in range(1, 11):
    num = float(input(f"{i}. Digite el numero: "))
    if num > 0:
        conteo_positivo += 1
    elif num < 0:
        conteo_negativo += 1
    else:
        conteo_neutro +=1

print(f"La cantidad de positivos es: {conteo_positivo}")
print(f"La cantidad de negativos es: {conteo_negativo}")
print(f"La cantidad de neutros es: {conteo_neutro}")