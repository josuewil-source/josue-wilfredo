# Crear agenda
agenda = {}

# Agregar contactos
agenda["Juan"] = "7777-1111"
agenda["María"] = "7777-2222"

# Buscar contacto
nombre = "Juan"

if nombre in agenda:
    print("Teléfono:", agenda[nombre])
else:
    print("Contacto no encontrado")

# Eliminar contacto
if nombre in agenda:
    del agenda[nombre]

print(agenda)
