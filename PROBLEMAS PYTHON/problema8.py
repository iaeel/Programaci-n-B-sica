import math

def calcular_circulo(radio):
    area = math.pi * radio ** 2
    circunferencia = 2 * math.pi * radio
    return area,circunferencia

# Entrada de datos
radio = float(input("Ingrese el radio del círculo: "))

# Cálculo del área y la circunferencia
area, circunferencia = calcular_circulo(radio)

# Impresión de resultados
print(f"El área del círculo es: {area:.2f}")
print(f"La circunferencia del círculo es: {circunferencia:.2f}")
