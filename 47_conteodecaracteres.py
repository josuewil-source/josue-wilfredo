# Texto
texto = "programacion en python"

# Diccionario
frecuencia = {}

# Contar caracteres
for caracter in texto:
    if caracter in frecuencia:
        frecuencia[caracter] += 1
    else:
        frecuencia[caracter] = 1

# Mostrar resultado
print(frecuencia)
