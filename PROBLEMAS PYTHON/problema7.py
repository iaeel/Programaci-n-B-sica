def verificar_numero(numero, divisor):
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")
    
    if numero % divisor == 0:
        print(f"{numero} es múltiplo de {divisor}.")
    else:
        print(f"{numero} no es múltiplo de {divisor}.")

# Entrada de datos
numero = int(input("Ingrese un número: "))
divisor = int(input("Ingrese el número para verificar múltiplo: "))

# Verificación del número
verificar_numero(numero, divisor)