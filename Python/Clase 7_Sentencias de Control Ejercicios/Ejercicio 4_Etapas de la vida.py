#Ejercicio 4: Etapas de lña vida
edad = int(input("Digite su edad: "))
mensaje = None
if 0 <= edad <10:
    mensaje = "La infancia es increible y bella"
elif 10 <= edad < 20:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
elif 30 <= edad < 40:
    mensaje = "Profesional y posiblemente familiar"
elif 40 <= edad < 50:
    mensaje = "Reflexion y nuevos retos personales"
elif 50 <= edad < 60:
    mensaje = "Madurez plena y experiencia"
elif 60 <= edad < 70:
    mensaje = "Disfrute del fruto del esfuerzo, tiempo para si mismo"
elif 70 <= edad < 80:
    mensaje = "Sabiduria y tranquilidad"
else:
    mensaje = "Opcion inválida. La edad no puede ser negativa."

print(f"Tu edad es: {edad}, {mensaje}")
