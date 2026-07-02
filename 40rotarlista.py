# Lista original
lista = [1, 2, 3, 4, 5]

# Posiciones a rotar
k = 2

# Ajustar si k es mayor que la longitud
k = k % len(lista)

# Rotar la lista
lista_rotada = lista[-k:] + lista[:-k]

# Mostrar resultado
print(lista_rotada)
