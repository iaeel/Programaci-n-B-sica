def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        #Agrega el valor actual de a (el término actual de la secuencia) a la lista secuencia.
        a, b = b, a + b
    return secuencia

def main():
    try:
        num_terminos = int(input("Ingresa el número de términos de la secuencia de Fibonacci: "))
        if num_terminos <= 0:
            print("Por favor, ingresa un número mayor que 0.")
        else:
            resultado = fibonacci(num_terminos)
            print(f"La secuencia de Fibonacci con {num_terminos} términos es: {resultado}")
            #Si el número es válido, llama a la función fibonacci con num_terminos como argumento y muestra el resultado.
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
        #Captura la excepción ValueError si el usuario ingresa algo que no es un número entero (por ejemplo, una letra) y muestra un mensaje de error.

if __name__ == "__main__":
    main()