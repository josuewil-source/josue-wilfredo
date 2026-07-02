# Crear banco
banco = {}

# Historial de transacciones
historial = []

# Crear cuentas
banco["1001"] = {
    "titular":"Juan",
    "saldo":500,
    "tipo":"Ahorro"
}

banco["1002"] = {
    "titular":"María",
    "saldo":300,
    "tipo":"Corriente"
}

# Depósito
banco["1001"]["saldo"] += 200
historial.append(("Depósito", "1001", 200))

# Retiro
if banco["1002"]["saldo"] >= 100:
    banco["1002"]["saldo"] -= 100
    historial.append(("Retiro", "1002", 100))

# Transferencia
if banco["1001"]["saldo"] >= 150:
    banco["1001"]["saldo"] -= 150
    banco["1002"]["saldo"] += 150
    historial.append(("Transferencia", "1001", "1002", 150))

# Mostrar cuentas
print("Cuentas:")
print(banco)

# Mostrar historial
print("\nHistorial:")
for movimiento in historial:
    print(movimiento)
