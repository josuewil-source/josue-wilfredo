# Texto a analizar
texto = """Python es un lenguaje de programación. Es muy popular en la actualidad. Python es versátil."""

# Separar palabras
palabras = texto.split()

# Número de palabras
print("Palabras:", len(palabras))

# Número de caracteres
print("Caracteres:", len(texto))

# Contar frecuencia de palabras
frecuencia = {}

for palabra in palabras:

    palabra = palabra.lower().strip(".,!?")

    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

# Palabra más frecuente
mas_frecuente = max(frecuencia, key=frecuencia.get)

print("Más frecuente:", mas_frecuente)

# Longitud promedio
total = 0

for palabra in palabras:
    total += len(palabra.strip(".,!?"))

print("Promedio:", total / len(palabras))

# Contar oraciones
oraciones = texto.split(".")

print("Oraciones:", len(oraciones) - 1)
