# Número a verificar
numero = 17

# Suponemos que el número es primo
es_primo = True

# Verificar divisores hasta la raíz cuadrada
for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        es_primo = False
        break

# Mostrar resultado
if es_primo:
    print("Es un número primo")
else:
    print("No es un número primo")
