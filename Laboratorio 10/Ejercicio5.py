"""
conversor_unidades.py
Módulo para conversión de unidades (simulado dentro de un solo archivo)
"""

def km_a_millas(km):
    """Convierte kilómetros a millas"""
    return km * 0.621371

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

def litros_a_galones(litros):
    """Convierte litros a galones"""
    return litros * 0.264172

# ==============================================
# Programa principal (simulando otro archivo)
# ==============================================

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\nCONVERSOR DE UNIDADES")
    print("1. Kilómetros a Millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a Galones")
    print("4. Salir")

def realizar_conversion(opcion):
    """Realiza la conversión según la opción seleccionada"""
    try:
        if opcion == '1':
            km = float(input("Ingrese kilómetros: "))
            print(f"\n{km} km = {km_a_millas(km):.4f} millas")
        elif opcion == '2':
            celsius = float(input("Ingrese grados Celsius: "))
            print(f"\n{celsius}°C = {celsius_a_fahrenheit(celsius):.2f}°F")
        elif opcion == '3':
            litros = float(input("Ingrese litros: "))
            print(f"\n{litros} litros = {litros_a_galones(litros):.4f} galones")
    except ValueError:
        print("\nError: Debe ingresar un valor numérico válido")

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == '4':
            print("\n¡Hasta luego!")
            break
        elif opcion in ('1', '2', '3'):
            realizar_conversion(opcion)
        else:
            print("\nOpción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    # Esto simula que estamos ejecutando el programa principal
    print("=== PROGRAMA PRINCIPAL DE CONVERSIÓN ===")
    main()