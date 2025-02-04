def es_primo(n): #Esta función verifica si un número n es primo.
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    elif n == 2:
        return True   # 2 es el único número par primo
    elif n % 2 == 0:
        return False  # Cualquier otro número par no es primo
    else:
        # Verificar divisibilidad desde 3 hasta la raíz cuadrada de n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False  # Si es divisible, no es primo
        return True  # Si no es divisible por ningún número, es primo
""" 
Si n es menor o igual a 1, devuelve False porque los números primos son mayores que 1.

Si n es 2, devuelve True porque 2 es el único número par primo.

Si n es par y mayor que 2, devuelve False porque ningún número par mayor que 2 es primo.

Para números impares mayores que 2, verifica si n es divisible por algún número impar desde 3 hasta la raíz cuadrada de n.

Si n es divisible por alguno de estos números, no es primo.

Si no es divisible por ninguno, es primo.
"""
def main():
    try:
        numero = int(input("Ingresa un número para verificar si es primo: "))
        if es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__": #Asegura que el programa solo se ejecute cuando se llama directamente, no cuando se importa como un módulo.
    main()