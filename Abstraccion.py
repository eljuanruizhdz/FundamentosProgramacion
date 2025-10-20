from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass


class Bisicleta(Vehiculo):
    pass


class Autobus(Vehiculo):
    pass


class Motoneta(Vehiculo):
    pass


class cuatrimoto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass
    

# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "n45", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
bisicleta1 = Bisicleta("BMC", "R20", 2023, "Negro")
autobus1 = Autobus("Marcopolo", "N303", 2020, "Azul")
motoneta1 = Motoneta("scooter", "D125", 2021, "Roja")
auto2 = Auto("Toyota", "At56", 2020, "Naranja")
moto2 = Moto("Italika", "HB", 2019, "Roja")


# Visualización
print(auto1)
print(moto1)
print(camion1)
print(bisicleta1)
print(autobus1)
print(motoneta1)
print(auto2)
print(moto2)