# Número inicial
numero = 1234

# Variable para almacenar la suma
suma = 0

# Extraer cada dígito
while numero > 0:
    suma += numero % 10
    numero //= 10

# Mostrar resultado
print("La suma de los dígitos es:", suma)
