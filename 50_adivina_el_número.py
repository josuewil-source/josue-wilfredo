# Importar librería
import random

# Generar número aleatorio
numero = random.randint(1,100)

intentos = 0

# Repetir hasta adivinar
while True:

    intento = int(input("Adivina el número: "))
    intentos += 1

    if intento == numero:
        print("¡Correcto!")
        print("Intentos:", intentos)
        break

    elif intento < numero:
        print("Muy bajo")

    else:
        print("Muy alto")
