# Paradigma imperativo
def calcular_factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# Paradigma estructurado
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Paradigma modular (simulando módulos)
class OperacionesMatematicas:
    @staticmethod
    def suma(a, b):
        return a + b
    
    @staticmethod
    def resta(a, b):
        return a - b

# Paradigma orientado a objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

def demostrar_paradigmas():
    print("Demostración de múltiples paradigmas de programación:")
    
    # Imperativo
    num = 5
    print(f"\nParadigma imperativo - Factorial de {num}: {calcular_factorial(num)}")
    
    # Estructurado
    print("\nParadigma estructurado - Números primos del 1 al 20:")
    for i in range(1, 21):
        if es_primo(i):
            print(i, end=" ")
    
    # Modular
    print("\n\nParadigma modular - Operaciones matemáticas:")
    print(f"Suma: 5 + 3 = {OperacionesMatematicas.suma(5, 3)}")
    print(f"Resta: 5 - 3 = {OperacionesMatematicas.resta(5, 3)}")
    
    # Orientado a objetos
    print("\nParadigma orientado a objetos:")
    persona = Persona("Juan", 30)
    persona.presentarse()

demostrar_paradigmas()