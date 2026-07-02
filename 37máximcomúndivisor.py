# Números
a = 48
b = 18

# Algoritmo de Euclides
while b != 0:
    a, b = b, a % b

# Mostrar resultado
print("El MCD es:", a)
