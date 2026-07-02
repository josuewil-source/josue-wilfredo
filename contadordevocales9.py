texto = "Hola Mundo Python"
vocales = "aeiou"
contador = 0

for letra in texto.lower():
    if letra in vocales:
        contador += 1

print("Cantidad de vocales:", contador)
