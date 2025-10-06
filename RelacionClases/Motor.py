class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def enceder(self):
        print("El motor", self.tipo, "está encendido.")
class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor("Electrico")

    def arrancar(self):
        print("El auto de marca", self.marca, "está arrancando.")
        self.motor.enceder()

auto1 = Auto("Tesla")
auto2 = Auto("Nissan")

auto1.arrancar() 
auto2.arrancar()       