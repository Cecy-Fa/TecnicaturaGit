# Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parámetro de la función
# y agregar como resultado la suma de todos los valores pasados como argumentos.
#Definimos una función
def sumar(*valores):
    suma = 0
    for valor in valores:
        suma = suma + valor
    print(suma)

sumar(1, 3, 4, 10, 15)

#Definimos una función (Video 10 explicativo del profe )
def sumar_valor(*args): #Recibimos una cantidad de parámetros indefinidos
    resultado = 0
    #Iteremos cada elemento
    for valor in args:
        resultado += valor
    return resultado

#Llamamos a la función
print(sumar_valor(1, 3, 4, 10, 15))
