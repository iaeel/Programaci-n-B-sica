def analizar_texto():
    texto = input("Ingrese un texto: ")
    palabras = texto.split()
    
    # Total de palabras
    total_palabras = len(palabras)
    
    # Palabras únicas
    palabras_unicas = set(palabras)
    total_unicas = len(palabras_unicas)
    
    # Frecuencia de palabras
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    # Palabra más frecuente
    palabra_mas_frecuente = max(frecuencia, key=frecuencia.get)
    veces_mas_frecuente = frecuencia[palabra_mas_frecuente]
    
    # Mostrar resultados
    print("\nResumen del análisis de texto:")
    print(f"Total de palabras: {total_palabras}")
    print(f"Palabras únicas: {total_unicas}")
    print("Frecuencia de palabras:")
    for palabra, count in frecuencia.items():
        print(f"'{palabra}': {count} veces")
    print(f"Palabra más frecuente: '{palabra_mas_frecuente}' ({veces_mas_frecuente} veces)")

analizar_texto()