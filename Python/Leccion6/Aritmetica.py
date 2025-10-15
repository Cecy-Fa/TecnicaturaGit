#CLASE 7 POO PARTE 2 SOLUCIÓN
#Crear la clase Aritmética: Sumar (video 3 Py)
class Aritmetica:
    '''
    El nombre de este tipo de comentario es: DocString
    esto es documentación de la clase en Python
    Vamos hacer en esta clase algunas operaciones de: suma, resta, multiplicación y más
    '''
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
#Método para sumar
    def sumar(sefl):
        return sefl.operandoA + sefl.operandoB
    
    def resta(sefl):
        return sefl.operandoA - sefl.operandoB
    
#Clase Aritmetica: Resta, multiplicación y división (video 4 Py)   
    def multiplicar(sefl):
        return sefl.operandoA * sefl.operandoB
    
    def dividir(sefl):
        return sefl.operandoA / sefl.operandoB

aritmetica1 = Aritmetica(7, 9) #Le pasamos los argumentos para los operandos
print(f'La suma de los numeros es: {aritmetica1.sumar()}')
print(f'La resta de los numeros es: {aritmetica1.resta()}')
print(f'La multiplicacion de los numeros es: {aritmetica1.multiplicar()}')
print(f'La division de los numeros es: {aritmetica1.dividir():.2f}')#siempre en las divisiones se genera un n° flotante
                                                            #por eso hay que colocarle(:.2f), para que no se muestren mas

#Creamos la clase: Rectángulo (video 5 Py)



