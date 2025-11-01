#Clase 9 POO Parte 5 Herencia Múltiple Solución
# Clase hija: Cuadrado (video 3Py)

from FiguraGeométrica import FiguraGeométrica
from Color import Color

# Clase hija: Cuadrado
class Cuadrado(FiguraGeométrica, Color):
    def __init__(self, lado, color):
        # super.__init__(lado)
        FiguraGeométrica.__init__(self, lado, lado)  # mismo valor para alto y ancho
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        #return f"Cuadrado de color {self.color}, lado = {self.alto}, área = {self.calcular_area()}"
        return f'{FiguraGeométrica.__str__ (self)}, {Color.__str__(self)}'