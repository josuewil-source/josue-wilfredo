# Registro
registro = {
    "Ana":{"Matemática":[8,9,10],"Inglés":[9,8]},
    "Luis":{"Matemática":[7,8],"Inglés":[10,9]}
}

# Promedio por estudiante
for estudiante in registro:

    suma = 0
    cantidad = 0

    for materia in registro[estudiante]:
        suma += sum(registro[estudiante][materia])
        cantidad += len(registro[estudiante][materia])

    print(estudiante, "Promedio:", suma/cantidad)
