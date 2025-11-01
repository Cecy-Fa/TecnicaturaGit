#Clase 9 POO Parte 5 Herencia Múltiple Solución
# Clase hija: Cuadrado (video 3Py)
# Clase Testear nuestro código: (video 4Py)

from Cuadrado import Cuadrado
from Leccion9.FiguraGeométrica import FiguraGeométrica
from Rectangulo import Rectangulo
# Ejemplo de uso

#Clase 10 POO Parte 6 Abstratic y Static
#Valoidaciones en atributos(video 1Py)
print('Creacion de objeto clase Cuadrado'.center(50, '_'))

#Clase 9 POO Parte 5 Herencia Múltiple Solución
# Clase hija: Cuadrado (video 3Py)
# Clase Testear nuestro código: (video 4Py)
cuadrado1 = Cuadrado(8, "Azul")
# Clase 10 POO Parte 6 Abstratic y Static
# Método encapsulado y setter (video 2 Py)
cuadrado1.alto = 7
cuadrado1.ancho = 7 # Clase 10 POO Parte 6 Abstratic y Static
                    # Explicación de validación setter (video 3 Py)

#print(cuadrado1.ancho)
#print(cuadrado1.alto)
print(f'Calcular el área del cuadrado: {cuadrado1.calcular_area()}') 

#Clase 9 POO Parte 5 Herencia Múltiple Solución
#MRO =Method Resolution Oder (video 6Py) indica el orden
print(Cuadrado.mro())

print(cuadrado1)
print('Creacion de objeto clase Rectangulo'.center(50, '_'))

#Clase 9 POO Parte 5 Herencia Múltiple Solución
#Creacion de la clase Rectángulo (video 8 y 9 PY)
rectangulo1 = Rectangulo(3, 9, "verde")

#Clase 10 POO Parte 6 Abstratic y Static
# Método encapsulado y setter (video 2 Py)
rectangulo1.ancho = 8

#Clase 9 POO Parte 5 Herencia Múltiple Solución
#Creacion de la clase Rectángulo (video 8 y 9 PY)
print(f'Calcular area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#Clase 10 POO Parte 6 Abstratic y Static
#Clases abstractas (video 5 Py)
#figura1 = FiguraGeométrica() #No se puede instanciar, es abstracta

#Clase 10 POO Parte 6 Abstratic y Static
#Atributo Read-only y método mro (video 6 PY)
#MRO =Method Resolution Oder: indica el orden
print(Cuadrado.mro())

