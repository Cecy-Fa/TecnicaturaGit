#Clase 9 POO Parte 5 Herencia Múltiple Solución
#Creacion de la clase Rectángulo (video 8 y 9 PY)
from Color import Color
from FiguraGeométrica import FiguraGeométrica

#Clase hija: Rectangulo
class Rectangulo(FiguraGeométrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeométrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeométrica.__str__(self)} {Color.__str__(self)}'
        #return f"Rectángulo de color {self.color}, alto = {self.alto}, ancho = {self.ancho}, área = {self.area()}"
