# Clase 11 POO 8 Diseño de clases y Sobrecarga de Operadores
# Prueba de las clases Orden y Producto (video 5 Py)

from Orden import *
from Producto import *

#creacion de productos
producto1 = Producto("Torta", 40000)
producto2 = Producto("Pescado", 10000)
producto3 = Producto("papa", 20000)
producto4 = Producto("Asado", 40000)

#agrupacion de productos para la orden
productos = [producto1, producto2] #Lista de productos
productos2 = [producto3, producto4]#Lista de productos

#orden
orden1 = Orden(productos)
orden2 = Orden(productos2)
#imprimir orden
print(orden1)
print(orden2)

#imprimir total
print(f' Total de la orden1: {orden1.calcularTotal()}')
print(f' Total de la orden2: {orden2.calcularTotal()}')

#agregar productos a una orden definida
orden2.productoLista(producto1)
orden2.productoLista(producto2)
print(orden2)
