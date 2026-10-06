# Actividad Nº9

# Variables a usar
agenda = {
    ("lunes", "10:00"): "Gimnasio",
    ("lunes", "16:00"): "Estudiar Programación",
    ("lunes", "19:00"): "Hockey",
    ("martes", "09:00"): "Trabajo",
    ("martes", "17:00"): "Estudiar Programación",
    ("martes", "20:00"): "Entrenamiento",
    ("miércoles", "10:00"): "Gimnasio",
    ("miércoles", "16:00"): "Estudiar Programación",
    ("miércoles", "19:00"): "Hockey",
    ("jueves", "09:00"): "Trabajo",
    ("jueves", "17:00"): "Estudiar Programación",
    ("jueves", "20:00"): "Entrenamiento",
    ("viernes", "10:00"): "Gimnasio",
    ("viernes", "16:00"): "Estudiar Programación",
    ("viernes", "19:00"): "Hockey",
    ("sábado", "11:00"): "Gimnasio",
    ("sábado", "17:00"): "Tiempo libre",
    ("domingo", "13:00"): "Almuerzo familiar",
    ("domingo", "18:00"): "Descanso",
}

print("--- Agenda semanal ---")

# Solicitud de inputs de busqueda
dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (Ejemplo 10:00): ")

clave = (dia, hora)

# Busqueda y resultados
if clave in agenda:
    print(f"La actividad es: {agenda[clave]}")
else:
    print("No hay ninguna actividad programada para ese día y hora")
