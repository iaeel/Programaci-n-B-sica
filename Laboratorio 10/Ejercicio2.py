inventario = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    producto = {
        'nombre': nombre,
        'categoria': categoria,
        'precio': precio,
        'cantidad': cantidad
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado al inventario.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in inventario[:]:
        if producto['nombre'] == nombre:
            inventario.remove(producto)
            print(f"Producto '{nombre}' eliminado.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def buscar_producto():
    nombre = input("Nombre del producto a buscar: ")
    for producto in inventario:
        if producto['nombre'] == nombre:
            print("\nInformación del producto:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            return
    print(f"Producto '{nombre}' no encontrado.")

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    
    inventario_ordenado = sorted(inventario, key=lambda x: x['precio'])
    print("\nInventario ordenado por precio:")
    for producto in inventario_ordenado:
        print(f"{producto['nombre']} - ${producto['precio']} - {producto['cantidad']} unidades")

def menu_inventario():
    while True:
        print("\nSistema de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            buscar_producto()
        elif opcion == '4':
            mostrar_inventario()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu_inventario()