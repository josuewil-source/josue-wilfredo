# Lista anidada
anidada = [[1, 2], [3, 4, 5], [6]]

# Lista donde se guardarán los elementos
plana = []

# Recorrer cada sublista
for sublista in anidada:
    for elemento in sublista:
        plana.append(elemento)

# Mostrar resultado
print(plana)
