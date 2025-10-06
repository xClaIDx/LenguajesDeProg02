import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"Estudiante registrado: {self.nombre} {self.edad} {self.carrera}")
         
    def mostrar_informacion(self):
        print(f"{self.nombre} estudia {self.carrera} y tiene {self.edad} años.")
              
    def __del__(self):
        print(f"El estudiante {self.nombre} ha sido eliminado.")


grupo = []  # lista de estudiantes

# Ingreso manual de estudiantes
while True:
    nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    
    try:
        edad = int(input("Ingrese la edad: "))
    except ValueError:
        print("La edad debe ser un número entero. Intente de nuevo.")
        continue
    
    carrera = input("Ingrese la carrera: ")
    
    estudiante = Estudiante(nombre, edad, carrera)
    estudiante.mostrar_informacion()
    grupo.append(estudiante)
    print("---- Estudiante agregado ----\n")

# Mostrar todos los estudiantes
print("\n📋 Lista de estudiantes registrados:")
for est in grupo:
    est.mostrar_informacion()

# Eliminar todos los estudiantes
grupo.clear()
del estudiante
gc.collect()

print("\nFin programa")
del estudiante
gc.collect()

