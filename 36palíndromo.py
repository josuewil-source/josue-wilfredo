# Texto a evaluar
texto = "Anita lava la tina"

# Eliminar espacios y convertir a minúsculas
texto = texto.replace(" ", "").lower()

# Comparar con su inverso
if texto == texto[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
