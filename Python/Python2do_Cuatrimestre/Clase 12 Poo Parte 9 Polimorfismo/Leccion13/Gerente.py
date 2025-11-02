#Clase 12 Poo Parte 9 Polimorfísmo
#Creamos la Clase Gerente (video 3 Py)

from Empleado import *

#Clase Hija
class Gerente(Empleado):
    def __init__(self, departamento, nombre, sueldo):

        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f"Gerente: [Departamento: {self.departamento}] {super().__str__()}"