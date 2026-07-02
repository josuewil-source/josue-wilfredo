# Lista de números
numeros = [1,2,3,4,5,6,7,8,9,10]

pares = []
impares = []

# Separar pares e impares
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Mostrar resultados
print("Pares:", pares)
print("Impares:", impares)
