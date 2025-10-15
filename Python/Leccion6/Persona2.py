#CLASE 8 POO PARTE 3: Métodos set y get solución: Persona2
#PARTE 1 Y 2 DE Métodos: SETTER: colocar, establecer, modificar (nos permiten modificar los atributos de una clase)
#                        GETTER: obtener o recuperar (Nos permiten obtener los atributos de una clase)
#Esto lo vamos a utilizar de alguna manera cuando no se puede acceder por un encapsulamiento
from symtable import Class
class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property #Decorador
    def nombre(self):#Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): #Método Setter
        print('Estamos utilizando el método set')# Método Setter, necesita un parámetro mas, porque este viene a modificar el valor para el atributo
        self._nombre = nombre

    @property #Decorador
    def apellido(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Método Setter
        print('Estamos utilizando el método set')
        self._apellido = apellido

    @property  #Decorador
    def edad(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._edad

    @edad.setter
    def edad(self, edad):  # Método Setter, necesita un parámetro mas, porque este viene a modificar el valor para el atributo
        print('Estamos utilizando el método set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ =='__main__':
    persona1 = Persona2('Cecilia', 'Farias', 40)
    print(persona1.nombre)#Llamamos al método getter
    print (persona1.mostrar_detalle())

#Parte 2 (video 2 Py)
    persona1.nombre = 'Juan Pedro' #Parametro del método sett
    print(persona1.nombre) #Otra vez con el método getter
    print(persona1.mostrar_detalle()) #Llamamos el método mostrar_detalle

#Atributo read-only (solo lectura) seria la edad porque no tiene el método set (video 3Py)
#persona1.edad = 43 #Esto no se debe colocar, da como error de atributo xq no se puede modificar atributo edad
#Cuando ya esta encapsulado la edad.
    print(persona1.edad)

print(__name__)







