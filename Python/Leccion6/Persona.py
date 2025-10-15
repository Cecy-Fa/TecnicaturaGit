#CLASE 6 POO Parte 1
#Creamos una clase (video 1Py)
'''class Persona:
    pass #Nose procesa nada más (No tiene contenido)
print(type(Persona))'''

#Atributos en métodos y creaciones de un objeto (video 2 Py)
class Persona: #Creamos una clase
    
    def __init__(self): #Se lo llama método Init Dunder
        self.nombre = 'Juan'
        self.apellido = 'Zalzar'
        self.edad = 22

persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

#Creacion de objetos con argumentos (video 3 Py)
class Persona: #Creamos una clase
    
    def __init__(self, nombre, apellido, dni, edad, *args, **wkargs): #Se lo llama método Init Dunder (De iniciacion)
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Este atributo esta encapsulado (guion bajo _dni) de una manera sugerida
        self.edad = edad
        self.args = args
        self.wkargs = wkargs

    def mostrar_detalle(self): #Self es igual a this.
        print(f'La clase persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad} la dirrecion es: {self.args}, los datos importantes son: {self.wkargs}')

persona1 = Persona('Cecilia', 'Farias', 32456987,40) # Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

#Creamos más objetos en una clase (video 4Py)
persona2 = Persona('Osvaldo', 'Giordanini', 30321456, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

#Tarea: Hacer el print igual que con el objeto
persona2 = Persona('Osvaldo', 'Giordanini', 56426845, 45)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

#Modificar atributos de un objeto (video 6 Py)
persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1  modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

#Método de instancia, crear UML=UNIFIED MODELIG LANGUAGE (Lenguaje Unificado de Lenguaje) (video7 Py)
#Los atributos son: características
#Los métodos son: el comportamiento que van a tener los objetos (acciones)

#Método de instancia: definimos un método (video 8 Py)
#La variables self solo se encuentra dentro de los métodos 
# def mostrar_detalle(self):
        #print(f'Perona: {self.nombre} {self.apellido} {self.edad}')
persona1.mostrar_detalle() #La referencia en este caso se pasa de manera automática
persona2.mostrar_detalle()

#CLASE 7 POO PARTE 2 SOLUCIÓN
#Palabra reservada self y atributos de instancia (video 1 Py)
#Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para self o dará error

#Crear atributos desde objetos (Video 2Py)
persona1.telefono = '11223344'
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}') #Hemos creado un atributo de un objeto
#print(persona2.telefono) #El objeto persona2 no tiene este atributo, da error

#Método Init Dunder(De iniciacion) con argumento variables video (7 Py)
#*args: argumentos variables para tuplas (Se pueden nombrar de otra manera también)
#**wkargs: argumentos variables para diccionarios
persona3 = Persona('Rogelio', 'Romero', 1234566, 22, 'Telefono', '111555222', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105,CFavorito='Azul', Auto='Citroen', Modelo=2021)
                                                                #Datos de tupla:.............................................................) #Datos de diccionario:{............................................}
persona3.mostrar_detalle()
#print(persona3._dni) #Esto no se debe utilizar (está encapsulado), esto dice que lo desconocemos Python

#Encapsulamiento PARTE 1 (video 8 Py) objetivo: no se puede acceder directamente a los atributos de la clase
#self._dni = dni #Este atributo está encapsulado (guion bajo _dni) de una manera sugerida

#Encapsulamiento PARTE 2 (video 9 Py)
#self.__nombre = nombre
#persona3.__nombre #Está totalmente encapsulado (doble guion bajo: __nombre)

#CLASE 8 POO PARTE 3: Métodos set y get solución: Persona2
#PARTE 1 Y 2 DE Métodos: SETTER: colocar, establecer, modificar (nos permiten modificar los atributos de una clase)
#                        GETTER: obtener o recuperar (Nos permiten obtener los atributos de una clase)
#Esto lo vamos a utilizar de alguna manera cuando no se puede acceder por un encapsulamiento
