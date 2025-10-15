#Uso de clases y módulos (Video 5 Py)

from Leccion6.Persona2 import Persona2 #Con el *también se pueden importar otras clases
print('Creacion de objetos'.center(50, '-'))
if __name__ == '__main__': #comprobacion para ver donde se esta ejecutando el código
    persona5 = Persona2('Lionel ','Messi ',38)
    persona5.mostrar_detalle()

#Comprobación del módulo principal en ejecución (video 6 Py)
    print(__name__) 

#Destructor de Objetos (video Py)
print('Eliminacion de objetos'.center(50,'-'))
del persona5
#def __del__(self):  esto se encuentra en carpeta Persona2 es lo que se elimina
    #print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')