# Inventario
inventario = {
    "Laptop": [(850,5)],
    "Mouse": [(25,20)],
    "Teclado": [(40,3)]
}

# Calcular valor total
valor_total = 0

for producto in inventario:
    for precio, stock in inventario[producto]:
        valor_total += precio * stock

print("Valor total:", valor_total)

# Mostrar productos con poco stock
print("Productos con bajo stock:")

for producto in inventario:
    for precio, stock in inventario[producto]:
        if stock < 5:
            print(producto)
