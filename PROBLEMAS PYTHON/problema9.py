def generar_listas_pares_impares(limite):
    pares = []
    impares = []
    for num in range(limite + 1):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

# Entrada de datos
limite = int(input("Ingrese el límite: "))

# Generación de listas
pares, impares = generar_listas_pares_impares(limite)

# Impresión de resultados
print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")
