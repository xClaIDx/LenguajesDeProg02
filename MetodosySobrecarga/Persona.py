class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

    def saludar(self):
        print(F"Hola, soy {self.nombre}")

persona1 = Persona("Carlos")
persona2= Persona(F"Maria")
persona1.saludar()
persona2.saludar()
