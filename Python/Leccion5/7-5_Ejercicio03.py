#Ejercicio03:
#Clase 5 FUNCIONES RECURSIVAS 3ra Parte (video 5 Py)
#Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
#valor de 5, debe imprimir:
#5
#4
#3
#2
#1
#En caso de ser el número 3 debe imprimir:
#3
#2
#1
#Si se ingresa número negativo no imprime nada

def mostrar_descendente(numero):
    if numero >= 1: #Caso base
        print(numero)
        mostrar_descendente(numero-1) #Caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Numero invalido.")

mostrar_descendente(5)