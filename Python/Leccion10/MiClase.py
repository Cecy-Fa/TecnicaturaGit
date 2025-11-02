#Clase 10 POO Parte 6 Abstrac y Static
#Variable de clase (video 8 Py)
class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'
    
    def __init__(self, variable_instancia): #La variable de instancia, da diferentes valores
        self.variable_instancia = variable_instancia

    # Clase 10 POO Parte 7 Constante y contexto estático
    # Método estático (video 2 Py)
    @staticmethod
    def metodo_estatico(): #Se asocia a la clase
        print(MiClase.variable_clase)

    # Clase 10 POO Parte 7 Constante y contexto estático
    # Método clase (video 3 Py)
    @classmethod
    def metodo_clase(cls): #cls: Referencia a la clase, se puede utilizar con cualquier nombre,
                            # por convención se usa cls
        print(cls.variable_clase)

    # Clase 10 POO Parte 7 Constante y contexto estático
    # Contexto estático y Dinámico (video 4 Py)
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

#Clase 10 POO Parte 6 Abstrac y Static
#Variable de clase (video 8 Py)
print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otro prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

#Clase 10 POO Parte 7 Constante y contexto estático
#Variable de clase (video 1 Py)
#ESTO EN VSCODE NO FUNCIONA BIEN. EN PYCHARM SI FUNCIONA
MiClase.variable_clase2 = 'Valor de variable de clase 2' #ESTO SI
print(MiClase.variable_clase2) #ESTO SI
#print(miClase1.variable_clase2) #ESTO NO
#print(miClase2.variabla_clase2) #ESTO NO

#Clase 10 POO Parte 7 Parte 7 Constante y contexto estático
#Método estático (video 2 Py)
MiClase.metodo_estatico()

#Clase 10 POO Parte 7 Parte 7 Constante y contexto estático
#Método clase (video 3 Py)
MiClase.metodo_clase()

#Clase 10 POO Parte 7 Constante y contexto estático
#Contexto estático y Dinámico (video 4 Py)
miObjeto1 = MiClase('Variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()