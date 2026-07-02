# Número decimal
decimal = 42

# Variable para guardar el binario
binario = ""

# Convertir usando divisiones sucesivas
while decimal > 0:
    residuo = decimal % 2
    binario = str(residuo) + binario
    decimal //= 2

# Mostrar resultado
print("Binario:", binario)
