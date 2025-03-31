def mergesort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        mergesort(izquierda)
        mergesort(derecha)
        
        i = j = k = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

def menu_mergesort():
    entrada = input("Ingrese una lista de números separados por espacios: ")
    numeros = [int(x) for x in entrada.split()]
    
    print("\nLista original:")
    print(numeros)
    
    mergesort(numeros)
    print("\nLista ordenada (Mergesort):")
    print(numeros)

menu_mergesort()