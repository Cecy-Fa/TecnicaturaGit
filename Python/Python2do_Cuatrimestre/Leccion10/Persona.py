# Clase 10 POO Parte 7 Parte Constante y contexto estático
#Ejercicio Contador (video 6 Py)
class Persona:
# CONTEXTO ESTÁTICO
    contador_personas = 0 # Variable de clase

    # Clase 10 POO Parte 7 Constante y contexto estático
    # Mejoras en el Ejercicio Contador(video 7 Py)
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas+=1 #vamos incrementando
        return cls.contador_personas

# Clase 10 POO Parte 7 Parte 7 Constante y contexto estático
# Ejercicio Contador(video 6 Py)
# CONTEXTO DINÁMICO
    def __init__(self, nombre, edad):
        #Persona.contador_personas += 1 # Vamos incrementando
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona: [ID:{self.id_persona}, Nombre: {self.nombre}, Edad: {self.edad}]'
    
persona1 = Persona('Ariel', 40)
print(persona1)
persona2 = Persona('Osvaldo', 45)
print(persona2)
persona3 = Persona('Liliana', 35)
print(persona3)

# Clase 10 POO Parte 7 Constante y contexto estático
# Ejercicio Contador(video 5 Py)
Persona.generar_siguiente_valor()
persona4 = Persona('Natalia', 35)
print(persona4)
print(f'Valor contador_personas: {Persona.contador_personas}')



