# Importar librerías
import random
import string

# Longitud de la contraseña
longitud = 12

# Caracteres disponibles
caracteres = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

# Generar contraseña
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

# Mostrar resultado
print("Contraseña:", contraseña)
