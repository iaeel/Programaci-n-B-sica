import random

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def menu_ordenamiento():
    n = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    numeros = [random.randint(1, 100) for _ in range(n)]
    
    print("\nLista original:")
    print(numeros)
    
    numeros_ordenados = quicksort(numeros)
    print("\nLista ordenada (Quicksort):")
    print(numeros_ordenados)
    
    objetivo = int(input("\nIngrese un número a buscar: "))
    posicion = busqueda_binaria(numeros_ordenados, objetivo)
    
    if posicion != -1:
        print(f"El número {objetivo} se encuentra en la posición {posicion}.")
    else:
        print(f"El número {objetivo} no está en la lista.")

menu_ordenamiento()