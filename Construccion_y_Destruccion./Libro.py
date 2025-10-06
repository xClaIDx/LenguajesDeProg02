import gc
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro registrado: {self.titulo} de {self.autor}, {self.anio}")
         
    def mostrar_informacion(self):
        print(f"'{self.titulo}' fue escrito por {self.autor} en el año {self.anio}.")
              
    def __del__(self):
        print(f"El libro '{self.titulo}' ha sido eliminado.")

libros_datos = []

while True:
    agregar = input("¿Desea agregar un libro? (s/n): ").strip().lower()
    if agregar == 'n':
        break
    elif agregar == 's':
        titulo = input("Ingrese el título del libro: ").strip()
        autor = input("Ingrese el autor del libro: ").strip()
        anio = input("Ingrese el año de publicación del libro: ").strip()
        try:
            anio = int(anio)
            libros_datos.append((titulo, autor, anio))
        except ValueError:
            print("El año debe ser un número. Intente nuevamente.")
    else:
        print("Opción no válida. Intente nuevamente.")

biblioteca = []  

for dato in libros_datos:
    libro = Libro(*dato)
    libro.mostrar_informacion()
    biblioteca.append(libro)

biblioteca.clear()
del libro
gc.collect()
print("\nFin programa")
