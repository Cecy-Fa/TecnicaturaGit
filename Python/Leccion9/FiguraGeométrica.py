#Clase 10 POO Parte 6 Abstratic y Static
#Clases abstractas (video 6 Py)
from abc import ABC, abstractmethod #ABC significa: Abstract Base Class, convierte una class en abstracta

#Clase 9 POO Parte 5 Herencia Múltiple Solución
# Clase padre: FiguraGeometrica (video 2Py)
class FiguraGeométrica (ABC):
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):# Clase 10 POO Parte 6 Abstratic y Static
                                        # Método encapsulado y setter (video 2 Py)
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erróneo para el ancho: {ancho}')# Clase 10 POO Parte 6 Abstratic y Static
                                                        # Método encapsulado y setter (video 2 Py)
        if self._validar_valores(alto): #Clase 10 POO Parte 6 Abstratic y Static
                                        #Método encapsulado y setter (video 2 Py)
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erróneo para el alto: {alto}')# Clase 10 POO Parte 6 Abstratic y Static
                                                        # Método encapsulado y setter (video 2 Py)

    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erróneo ancho: {ancho}')# Clase 10 POO Parte 6 Abstratic y Static
                                                    # Explicación de validación setter (video 3 Py)
        
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'Valor erróneo ancho: {alto}')# Clase 10 POO Parte 6 Abstratic y Static
                                                # Explicación de validación setter (video 3 Py)
    
    #Clase 10 POO Parte 6 Abstratic y Static
    #Clases abstractas (video 5 Py)
    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'FiguraGeométrica -> Alto: {self._alto}, Ancho: {self._ancho}'

    # Clase 10 POO Parte 6 Abstratic y Static
    # Método encapsulado y setter (video 2 Py)
    def _validar_valores(self, valor): #Se utiliza este método en la clase padre solo interna
        return  True if 0 < valor < 10 else False


