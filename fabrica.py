#crear una clase fabrica q tenga los atributos llantas , color , y precio ; luego crear dos clases que hereden de fábrica , las cuales son moto  y carro, crear métodos que muestren la cantidad de llantas color y precio
# Clase Fabrica
class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_datos(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")

    def aplicar_descuento(self):
        if self.precio > 100000:
            self.precio *= 0.10
            print("Se ha aplicado un descuento del 10%")
  

# Clase Moto que hereda de Fabrica
class Moto(Fabrica):
    def __init__(self, llantas, color, precio, cilindrada):
        super().__init__(llantas, color, precio)
        self.cilindrada = cilindrada

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Cilindrada: {self.cilindrada}")

# Clase Carro que hereda de Fabrica
class Carro(Fabrica):
    def __init__(self, llantas, color, precio, capacidad_pasajeros):
        super().__init__(llantas, color, precio)
        self.capacidad_pasajeros = capacidad_pasajeros

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")

# Crear objetos
moto = Moto(2, "Rojo", 20000, 250)
carro = Carro(4, "Azul", 150000, 5)

# Mostrar datos
print("Moto:")
moto.mostrar_datos()
moto.aplicar_descuento()
moto.mostrar_datos()

print("\nCarro:")
carro.mostrar_datos()
carro.aplicar_descuento()
carro.mostrar_datos()
