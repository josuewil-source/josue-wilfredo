# Rango de búsqueda
inicio = 10
fin = 50

# Lista donde se guardarán los primos
primos = []

# Buscar números primos
for numero in range(inicio, fin + 1):
    es_primo = True

    if numero < 2:
        es_primo = False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(numero)

# Mostrar resultado
print(primos)
