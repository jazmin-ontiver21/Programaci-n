class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
   
    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
   
    def resultado(self):
        if self.nota >= 7:
            NOTA = "Aprobado"
        else:
            NOTA = "No Aprobado"
        print(f"{self.nombre} ha {NOTA} con una nota de {self.nota}.")


alumno1 = Alumno("Pia Siri", 8)
alumno1.imprimir_datos()
alumno1.resultado()


alumno2 = Alumno("Mia Torres", 7)
alumno2.imprimir_datos()
alumno2.resultado()


alumno3 = Alumno("Anna Chavez", 4)
alumno3.imprimir_datos()
alumno3.resultado()
