#Clase 11 POO 8 Diseño de clases y Sobrecarga de Operadores
#Clase Producto (video 2 Py)
from Producto import *
class Orden(Producto):
    contadorOrdenes = 0
    def __init__(self, producto):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._producto = list(producto)

# Clase 11 POO 8 Diseño de clases y Sobrecarga de Operadores
# Clase Orden Parte 1 (video 2 Py)
    #Añadimos productos a una lista
    def productoLista(self, producto):
        self._producto.append(producto) #Esto es para agregar un nuevo producto

# Clase 11 POO 8 Diseño de clases y Sobrecarga de Operadores
# Clase Orden Parte 2 (video 3 Py)
    #Caculamos el total
    def calcularTotal(self):
        total = 0
        for producto in self._producto:
            total += producto.precio
        return total

# Clase 11 POO 8 Diseño de clases y Sobrecarga de Operadores
# Clase Orden Parte 2 (video 3 Py)
    #imprimimos
    def __str__(self):
        productos_str = ""
        for producto in self._producto:
            productos_str += producto.__str__() + "|" #Símbolo "|" Pay
        return f"Orden: {self._idOrden}, Productos = {productos_str}"

if __name__ == "__main__":
    torta = Producto("Torta", 40000)
    pescado = Producto("Pescado", 10000)
    print(torta.__str__())
    print(pescado.__str__())
    productos = [torta, pescado] #Lista de productos
    orden1 = Orden(productos) #Primer objeto orden pasamos la lista de productos
    print(orden1)

    # Clase 11 POO 8 Diseño de clases y Sobrecarga de Operadores
    # Clase Orden Parte 3 (video 4 Py)
    orden2 = Orden(productos)
    print(orden2)