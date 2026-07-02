# Número de filas
filas = 4

# Crear la pirámide
for i in range(1, filas + 1):

    # Espacios al inicio
    print(" " * (filas - i), end="")

    # Números ascendentes
    for j in range(1, i + 1):
        print(j, end="")

    # Números descendentes
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
