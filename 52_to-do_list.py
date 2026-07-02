# Lista de tareas
tareas = []

# Agregar tareas
tareas.append({"nombre":"Estudiar Python","prioridad":1,"estado":"Pendiente"})
tareas.append({"nombre":"Hacer tarea","prioridad":2,"estado":"Pendiente"})

# Marcar una tarea como completada
tareas[0]["estado"] = "Completada"

# Eliminar una tarea
del tareas[1]

# Mostrar tareas
for tarea in tareas:
    print(tarea)
