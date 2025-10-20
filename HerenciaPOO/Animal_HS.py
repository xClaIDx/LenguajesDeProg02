class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacerSonido(self):
        return "¡Guau Guau!"
    
class Gato(Animal):
    def hacerSonido(self):
        return "¡Miau Miau!"

perro = Perro("Rex")
print(f"{perro.nombre} dice {perro.hacerSonido()}")

gato = Gato("Mishi")
print(f"{gato.nombre} dice {gato.hacerSonido()}")
