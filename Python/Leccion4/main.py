#Clase 1: Colecciones Parte 1

#Listas Parte 1 (video 1 Python), se las conoce en otros lenguajes como arreglos o vectores

#lista = Ariel, Liliana, Natalia, Osvaldo (conjunto de elemntos)
'''nombre = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombre)
print(nombre[0])
print(nombre[3])
print(nombre[-1])

#Listas Parte 2 (video 2 Python)
#Recuperar un rango de la lista
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2]) #solo muestra el indice 0,1 pero no el indice 2
#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indices a mostrar 0,1,2
#Desde el indice indicadi el final
print(nombres[1: ])
#Modificar un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('se acabaron los elemntos de la lista')


#Listas Parte 3 (video 3 Python)
#preguntamos cuantos elementos tiene
print(len(nombres)) #le pasamos como parametro la lista

#Agregamos un elemento (puede tener varios elementos (booleano, flotante, n° entero, otra lista))
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

#Insertar un elemento en un indice especifico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Debora')
print(nombres)

#Eliminamos un elemnto
nombres.remove('Alberto')
print(nombres)

#Eliminar el ultimo elemnto de la lista
nombres.pop()
print(nombres)
#Eliminarun indice especifico
del nombres[2] #Significa delete (eliminar)
print(nombres)
#Eliminar, borrar o limpiar todos los elemntos
nombres.clear()
print(nombres)
#Eliminar la lista
del nombres
#print(nombres)#Aqui nos mostrará un error


#Tuplas Parte 1 (video 6 Python)
#Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor') #Tupla al ejecutarlo siempre debe tener a un que sea un elemento: la coma ('...' ,)
print(cocina)
print(len(cocina))

#Acceder a un elemnto, para esto utilizamos corchetes No parentesis
print(cocina[0])
#Mostrar de manera inversa
print(cocina[-1])
#Acceder a un rango
print(cocina[0:1])
#ejemplo
verduras = ('papa')#Tipo string cadena no lleva esto ('...' ,), solo el nombre simple ej: papa
print(verduras)

#Tuplas Parte 2 (video 7 Python)
#Recorrecemos los elemntos de la Tupla
for cocinar in cocina: #Print esta usando \n para saltos de lineas
    print (cocinar, end=' ') #usamos end= para eliminar los saltos de linea
#En las tuplas no se pueden utilizar LAS FUNCIONES: appen, insert, remover
#Modificamos Un Tupla a lista o bisceversa
cocinaLista = list(cocina)
cocinaLista [0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

#Eliminamos una Tupla
#del cocina
#print(cocina)

#CLASE 2: COLECCIONES PARTE 2
#Tipos Set (video 1 Python); 
#El orden es aleatorio. Un elemento de tipo set: es una coleccion sin orden y sin indice.
planetas = {'Martes', 'Jupiter', 'Venus'}
print(len(planetas))#Len = length significa largo () nos indica la cantidad de elementos)

#Revisar si un elemnto existe dentro del set
print('Martes' in planetas)# esta este planeta? verdadero o falso

#Agregar un elemnto
planetas.add('Tierra') #add es una función
print(planetas)


#Tipos Set o conjuntos (video 2 Python); 
#Eliminar elemntos, puede arrojar un error si el elemnto no existe
planetas.remove('Jupiter')#Esta función ante de un mal ingreso u inexistente del elemnto da error
print(planetas)
planetas.discard('Tierra')#Esta función no nos presenta ningun error
print(planetas)

#Limpiar set o conjunto
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas #Al eliminar nos muestra un error

#Diccionario Parte 1 de PYTHON (video 3 Python)
##Esta compuesto por dos elementos
#'Maradona': 10 //Tipo cadena 1ro 'Maradona' y 2do tipo numerico 10
#dict (key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}

#Verificamos la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave (Key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos los elementos
diccionario['IDE'] = 'Entorno  de Desarrollo Integrado'
print(diccionario)


#Diccionario Parte 2 de PYTHON (video 4 Python)
#Como recorrer los elemntos
for termino in diccionario: #Recorremos mostrando solo llaves
    print(termino)

#for termino, valor in diccionario:
#    print(termino, valor)#No se puede acceder al valor, sale error

#Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de accdeder a un diccionario
for termino in diccionario.keys():
    print(termino) #Muestra solo las llaves


#Usamos una función para acceder al valor
for valor in diccionario.values():
    print(valor)

#Comprobar la existencia de algun elemento
print('IDE' in diccionario)#Devuelve un booleano

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Eliminar un elemento un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario 
#del diccionario #Diccionario se borro

#Repaso y más conceptos de Listas (video 5 Python)
#Agregamos un elemento (puede tener varios elementos (booleano, flotante, n° entero, otra lista))
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)'''

#Concatenar listas (video 6 Python)
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2 #Concatenación
print(lista3)

lista3.extend([7, 8, 9, 1])# Funcion para agregar varios elementos a una lista
print(lista3)
print(lista3.index(5))#Funcion para ubiacar en que indice esta el valor ingresado
#print(lista3.index(0)) #esto daria un error por no ser el elemento parte de la lista

#como saber cuamtos valores repetidos hay dentro de una lista
print(lista3.count(1)) #cuenta cuantos valores iguales hay dentro de la lista

#Para poner el reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elemntos (video 7 Python)
lista3 =lista3 * 2
print(lista3)

#Métodos de ordenamiento, en  Python es una función 
lista3.sort() #Ordena los elemntos ascendentemente
print (lista3)
lista3.sort(reverse=True) #Ordena los elemntos descendentemente
print(lista3)

# Repaso de las  TUPLAS (video 8 Python)
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') #Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) #Accion booleana, su respuesta es de tipo booleana
#Lo que podemos usar dentro de tuplas son: index, count, len
#En tuplas se puede convertir de tupla a lista y de lista a tupla 
