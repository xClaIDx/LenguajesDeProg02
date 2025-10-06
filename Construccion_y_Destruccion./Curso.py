import gc
class Curso:
    def __init__(self, nombre,codigo,profesor):  
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        print(f"Curso registrado: {self.nombre} - Código: {self.codigo}, Profesor: {self.profesor}")

    def mostrar_informacion(self):
        return f"Curso: {self.nombre} - Código: {self.codigo}, Profesor: {self.profesor}\n"
    
    def __del__(self):
        print(f"El curso '{self.nombre}' ha sido eliminado.")

cursos = [] 

while True:
    agregar = input("¿Desea agregar un curso? (s/n): ").strip().lower()
    if agregar == 'n':
        break
    elif agregar == 's':
        nombre = input("Ingrese el nombre del curso: ").strip()
        codigo = input("Ingrese el código del curso: ").strip()
        profesor = input("Ingrese el nombre del profesor: ").strip()
        cursos.append((nombre, codigo, profesor))
    else:
        print("Opción no válida. Intente nuevamente.")

for dato in cursos:
    curso = Curso(*dato)
    print(curso.mostrar_informacion())

cursos.clear()
del curso
import gc
gc.collect()
print("\nFin programa")
