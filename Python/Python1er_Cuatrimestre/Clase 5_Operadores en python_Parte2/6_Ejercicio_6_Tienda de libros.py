"""Ejercicio: Tienda de libros
1_Mostrar: Ingrese los siguientes datos del libro
2_Digite el nombre del libro
3_Digite el ID del libro
4_Digite el precio del libro
5:Indicar si el envio es gratuito (True/False)
6_Mostrar:
Nombre:
ID:
Precio:
Envio Gratuito?:
"""
print("Digite los siguientes datos del libro")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el envio es gratuito (True/False): ")
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"
print(f'''
        Nombre: {nombre}
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
''')