# Clase padre Calzado
class Calzado:
    def __init__(self, fecha_de_creacion, origen, marca, tipo, nro, suela):
        self.fecha_de_creacion = fecha_de_creacion
        self.origen = origen
        self.marca = marca
        self.tipo = tipo
        self.nro = nro
        self.suela = suela

    def __str__(self):
        return f"Calzado: {self.marca} {self.tipo} - Fecha de creación: {self.fecha_de_creacion}"

# Clase hija Zapato
class Zapato(Calzado):
    def __init__(self, fecha_de_creacion, origen, marca, tipo, nro, suela, numero, modelo, materiales, stock):
        super().__init__(fecha_de_creacion, origen, marca, tipo, nro, suela)
        self.numero = numero
        self.modelo = modelo
        self.materiales = materiales
        self.stock = stock

    def __str__(self):
        return f"{super().__str__()} - Número: {self.numero} - Modelo: {self.modelo} - Materiales: {self.materiales} - Stock: {self.stock}"

# Ejemplo de uso
zapato = Zapato("2022-01-01", "China", "Nike", "Deportivo", "12345", "Goma", 42, "Air Max", "Cuero y goma", 100)
print(zapato)