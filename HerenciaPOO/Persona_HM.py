class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
class Trabajador:
    def __init__(self,profesion,salario):
        self.profesion = profesion
        self.salario = salario  

    def trabajar(self):
        return f"Estoy trabajando como {self.profesion} y gano ${self.salario} al mes."
    
class Estudiante:
    def __init__(self,carrera,universidad):
        self.carrera = carrera
        self.universidad = universidad

    def estudiar(self):
        return f"Estudio {self.carrera} en la  {self.universidad}."
    
class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def mostrar_info(self):
        return (f"\n{self.presentarse()}\n"
                f"{self.trabajar()}\n"
                f"{self.estudiar()}\n")
    
def main():
    persona1 = PersonaMultirol(
        nombre="Juanita",
        edad=25,
        profesion="Desarrolladora de Software",
        salario=2500,
        carrera="Ingenieria Estadistica e Informática",
        universidad="Universidad Nacional del Altiplano"
    )

    print(persona1.mostrar_info())
if __name__ == "__main__":
    main()
