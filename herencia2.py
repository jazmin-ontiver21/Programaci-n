class Person:
   def __init__(self, fname, lname, dni, direccion, codigo_postal, fechaNacimiento):
       self.firstname = fname
       self.lastname = lname
       self.dni =dni
       self.direccion = direccion
       self.codigo_postal = codigo_postal
       self.fechaNacimiento = fechaNacimiento




   def printname(self):
       print(self.firstname, self.lastname)




   def print_details(self):
       print(f"Nombre: {self.firstname} {self.lastname}")
       print(f"DNI: {self.dni}")
       print(f"Dirección: {self.direccion}")
       print(f"Código Postal: {self.codigo_postal}")
       print(f"Fecha de Nacimiento: {self.fechaNacimiento}")

x1 = Person("Malena", "41234728", "jonh kennedy 345", "5280", "09/10/2007")
x2 = Person("Pedro", "Lopez", "6885943", "yrigoyen", "5280", "01/02/2003")
x3 = Person("Ana", "Martinez", "1109584", "ataliva herrera", "5280", "03/04/2001")



x1.print_person_details()
print()
x2.print_person_details()
print()
x3.print_person_details()
print()