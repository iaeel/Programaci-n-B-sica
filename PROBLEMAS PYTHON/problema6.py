def interes_compuesto(capital, tasa, tiempo):
    monto = capital
    t = 0
    while t < tiempo:
        monto *= (1 + tasa / 100)
        t += 1
    return monto

# Entrada de datos
capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés (%): "))
tiempo = int(input("Ingrese el tiempo en años: "))

# Cálculo e impresión del resultado
monto_final = interes_compuesto(capital, tasa, tiempo)
print(f"El monto final después de {tiempo} años es: {monto_final:.2f}")
