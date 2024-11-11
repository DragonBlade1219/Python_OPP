# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido")

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        print("El perro ladra")

# Uso de las clases
mi_animal = Animal("Genérico")
mi_animal.hacer_sonido()
print(mi_animal.nombre)

mi_perro = Perro("Fido")
mi_perro.hacer_sonido()
print(mi_perro.nombre)

