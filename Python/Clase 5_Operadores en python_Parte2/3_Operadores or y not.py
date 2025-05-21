"""Ejercicio: Operador or, Operador not
La pregunta es si un padre puese
asistir al juego de su hijo.
1_Verificamos si tiene vacaciones
2_Verificamos si tiene el día libre
3_Usar estructura "If else" con el operador
4_Imprimir
"""
vacaciones = True
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Tiene trabajo que hacer")
else:
    print("Puede asistir al juego")
