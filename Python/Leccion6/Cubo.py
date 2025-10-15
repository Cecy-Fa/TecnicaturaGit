#Creamos la clase: Cubo (video 6 Py)
"""
Crear la clase Cubo con los atributos, ancho, alto y profundidad,
con un método calcular_volumen que tendrá la formula:
volumen = ancho * altura * profundidad
que el usuario ingrese los valores
"""
class Cubo:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        print(f"El volumen del Cubo es: {self.ancho * self.altura * self.profundidad}")

cubo = Cubo(altura=0, ancho=0, profundidad=0)
print("Ingrese las siguientes medidas del Cubo para calcular el volumen:")
cubo.ancho = float(input("Ancho: "))
cubo.altura = float(input("Altura: "))
cubo.profundidad = float(input("Profundidad: "))
cubo.calcular_volumen() #El resultado da con coma(30.0)

#Como lo desarrolla el Profe:
class Cubo:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad
    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input('Digite el ancho del cubo: '))
altura = int(input('Digite la altura del cubo: '))
profundidad = int(input('Digite la profundidad del cubo: '))

cubo1 = Cubo(altura, ancho, profundidad)
print(f'El valor del cubo es: {cubo1.calcular_volumen()}') #El resultado da sin coma (30)