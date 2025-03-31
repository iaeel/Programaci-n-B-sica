class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio: ${self.precio}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, num_puertas):
        super().__init__(marca, modelo, año, precio)
        self.num_puertas = num_puertas
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self.num_puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada}cc")

# Ejemplo de uso
auto = Automovil("Toyota", "Corolla", 2022, 25000, 4)
moto = Motocicleta("Honda", "CBR600", 2021, 12000, 600)

print("\nInformación del automóvil:")
auto.mostrar_info()

print("\nInformación de la motocicleta:")
moto.mostrar_info()