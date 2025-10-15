class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro {self.titulo} ha sido prestado")
        else:
            print(f"El libro {self.titulo} no está disponible")

    def devolver(self):
        self.disponible = True
        print(f"El libro {self.titulo} ha sido devuelto")

class Prestamo:
    def __init__(self, libro, fecha_prestamo):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.devuelto = False

    def marcar_devolucion(self):
        self.devuelto = True
        self.libro.devolver()  

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []

    def realizar_prestamo(self, libro, fecha):
        if libro.disponible:
            libro.prestar()
            prestamo = Prestamo(libro, fecha)
            self.prestamos.append(prestamo)
        else:
            print("No se puede realizar el préstamo del libro. No disponible")

    def mostrar_prestamo(self):
        print(f"Préstamos de {self.nombre}:")
        for p in self.prestamos:
            estado = 'Devuelto' if p.devuelto else 'Pendiente'
            print(f"{p.libro.titulo} - {estado} - Fecha: {p.fecha_prestamo}")

def main():
    nombLibro = input("Ingrese el nombre del libro: ")
    autor0 = input("Ingrese el autor del libro: ")
    isbn0 = input("Ingrese el ISBN del libro: ")

    libro0 = Libro(nombLibro, autor0, isbn0)
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "12345")
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "67890")

    usuario1 = Usuario("Juan Perez", "U123")
    usuario2 = Usuario("Maria Gomez", "U456")

    usuario1.realizar_prestamo(libro1, "2025-13-10")
    usuario1.prestamos[0].marcar_devolucion()

    usuario1.realizar_prestamo(libro2, "2025-29-10")
    usuario1.prestamos[1].marcar_devolucion()

    usuario2.realizar_prestamo(libro0, "2025-15-11")
    usuario2.prestamos[0].marcar_devolucion()  # ✅ índice corregido

    usuario1.mostrar_prestamo()
    usuario2.mostrar_prestamo()

if __name__ == "__main__":
    main()