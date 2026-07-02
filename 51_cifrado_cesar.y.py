# Mensaje y desplazamiento
mensaje = "Hola Mundo"
desplazamiento = 3

# Variable para guardar el mensaje cifrado
resultado = ""

# Recorrer cada carácter
for letra in mensaje:

    if letra.isalpha():

        if letra.isupper():
            inicio = ord("A")
        else:
            inicio = ord("a")

        nueva = chr((ord(letra) - inicio + desplazamiento) % 26 + inicio)
        resultado += nueva

    else:
        resultado += letra

# Mostrar resultado
print("Mensaje cifrado:", resultado)
