class Persona:
    def __init__ (self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self nombre},{self.edad} años "
persona1 = Persona ("Carlos",30)
persona2 = Persona ("Ana", 25)
persona3 = Persona ("Lucia", 30)

print (persona1)
print (persona2)
print (persona3)