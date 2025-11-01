#Clase 9 POO Parte 4 Herencia Tarea
#Clase 9 POO Parte 4 Herencia SOLUCIÓN
#Herencia: Tarea (video 3 Py) 

class Persona:  # Clase Padre,esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):  # Método Getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método Setter
        self._nombre = nombre

    @property
    def edad(self):  # Método Getter
        return self._edad

    @edad.setter
    def edad(self, edad):  # Método Setter
        self._edad = edad

    def __str__(self): #Override = sobreescribir
        return f'Persona: [ Nombre: {self._nombre}, Edad: {self._edad}]'

class Empleado(Persona):  #Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._edad} {self._sueldo}")

    @property
    def sueldo(self):  # Método Getter
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):  # Método Setter
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [ Sueldo: {self._sueldo}] {super().__str__()}'

empleado1 = Empleado('Cecilia', 40, 95000)
print(empleado1)
print(empleado1._nombre)
print(empleado1._edad)
print(empleado1._sueldo)


#Clase 9 POO Parte 4 Herencia SOLUCIÓN
# 11.4 Herencia: Tarea: (video 4 Py)
#Encapsular los atributos y agregar los métodos getters and setters
#Crear otro objeto, pasar los datos para nombre, edad, y sueldo
#mostrar estos datos, luego modificar y mostrar nuevamente
empleado2 = Empleado('Abbi', 35, 100000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
empleado2.nombre = 'Felipe'
empleado2.edad = 24
empleado2.sueldo = 50000
empleado2.mostrar_detalles()