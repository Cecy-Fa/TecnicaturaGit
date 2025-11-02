# Clase 11 POO 8 Diseño de clases y Sobrecarga de Operadores
# Sobrecarga de Operadores Parte 2a (video 8 Py)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __add__(self,other):   #Suma #Other significa = otro
        #se define con que trabajara
        return f"{self.nombre} {other.nombre}"

    # Sobrecarga de Operadores Parte 2b (video 9 Py)
    def __sub__(self, other):   #Resta #Other significa = otro
        #se define con que trabajara
        return self.edad - other.edad


persona1 = Persona("Cecilia", 19)
persona2 = Persona("Farias", 5)

#persona1.__add__(persona2) sintaxis interna y automática

#imprime la suma de los nombres
print(persona1 + persona2)

#imprime la resta de los años
print(persona1 - persona2)