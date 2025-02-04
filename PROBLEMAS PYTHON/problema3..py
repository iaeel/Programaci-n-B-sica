def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        numero = int(input("Ingresa un número para calcular su factorial: "))
        if numero < 0:
            print("El factorial no está definido para números negativos.")
        else:
            resultado = factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()