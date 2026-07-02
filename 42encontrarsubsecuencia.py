# Lista principal y subsecuencia
lista_principal = [1, 2, 3, 4, 5, 6]
subsecuencia = [2, 4, 6]

# Índice para recorrer la subsecuencia
indice = 0

# Buscar la subsecuencia
for numero in lista_principal:
    if indice < len(subsecuencia) and numero == subsecuencia[indice]:
        indice += 1

# Mostrar resultado
if indice == len(subsecuencia):
    print("Sí es una subsecuencia")
else:
    print("No es una subsecuencia")
