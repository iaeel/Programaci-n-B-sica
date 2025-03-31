import math

def calcular_estadisticas(*args):
    numeros = list(args)
    n = len(numeros)
    
    if n == 0:
        return None, None, None
    
    # Promedio (usando lambda)
    promedio = (lambda x: sum(x)/len(x))(numeros)
    
    # Mediana
    numeros_ordenados = sorted(numeros)
    if n % 2 == 1:
        mediana = numeros_ordenados[n//2]
    else:
        mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    
    # Desviación estándar
    suma_cuadrados = sum((x - promedio) ** 2 for x in numeros)
    desviacion = math.sqrt(suma_cuadrados / n)
    
    return promedio, mediana, desviacion

def menu_estadisticas():
    entrada = input("Ingrese una lista de números separados por espacios: ")
    numeros = [float(x) for x in entrada.split()]
    
    promedio, mediana, desviacion = calcular_estadisticas(*numeros)
    
    print("\nResultados:")
    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")
    print(f"Desviación estándar: {desviacion}")

menu_estadisticas()
