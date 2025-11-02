#Clase 12 Poo Parte 9 Polimorfísmo
#Creamos la Clase Empleado (video 2 Py)
#Clase padre
class Empleado: #No hereda si no solo de la Clase Objeto
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleado: [nombre: {self.nombre}, sueldo: {self.sueldo}]"

# Clase 12 Poo Parte 9 Polimorfísmo
#Prueba con otro objeto y método (video 5 Py)
    def mostrarDetalle(self):
        return self.__str__()
