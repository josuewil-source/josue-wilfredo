# Diccionarios
dict1 = {"a":10,"b":20,"c":30}
dict2 = {"b":15,"c":25,"d":35}

# Copiar primer diccionario
resultado = dict1.copy()

# Unir los diccionarios
for clave, valor in dict2.items():
    if clave in resultado:
        resultado[clave] += valor
    else:
        resultado[clave] = valor

# Mostrar resultado
print(resultado)
