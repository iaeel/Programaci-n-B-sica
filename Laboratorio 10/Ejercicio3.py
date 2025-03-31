agenda = []

def agregar_contacto():
    nombre = input("Nombre del contacto: ")
    numero = input("Número de teléfono: ")
    correo = input("Correo electrónico: ")
    
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    print(f"Contacto '{nombre}' agregado.")

def buscar_contacto():
    nombre = input("Nombre del contacto a buscar: ")
    encontrado = False
    
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            print("\nDetalles del contacto:")
            print(f"Nombre: {contacto[0]}")
            print(f"Teléfono: {contacto[1]}")
            print(f"Correo: {contacto[2]}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"Contacto '{nombre}' no encontrado.")

def listar_contactos():
    if not agenda:
        print("La agenda está vacía.")
        return
    
    agenda_ordenada = sorted(agenda, key=lambda x: x[0].lower())
    print("\nLista de contactos (orden alfabético):")
    for contacto in agenda_ordenada:
        print(f"{contacto[0]} - Tel: {contacto[1]} - Email: {contacto[2]}")

def menu_agenda():
    while True:
        print("\nAgenda de Contactos")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            buscar_contacto()
        elif opcion == '3':
            listar_contactos()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu_agenda()