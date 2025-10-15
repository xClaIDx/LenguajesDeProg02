class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" ha sido devuelto')
    def devolver(self):
        self.disponible = True
        print(f'El libro "{self.titulo}" ha sido devuelto.')

class Prestamo:
    def __init__(self, libro, fecha_prestamo):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.devuelto = False

    def marcar_devuelto(self):
        self.devuelto = True
        self.libro.devolver()

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []

    def realizar_prestamo(self, libro, fecha_prestamo):
        if libro.disponible:
            prestamo = Prestamo(libro, fecha_prestamo)
            self.prestamos.append(prestamo)
            libro.prestar()
        else:
            print(f'El libro "{libro.titulo}" no está disponible para préstamo.')
    def mostrar_prestamos(self):
        for prestamo in self.prestamos:
            estado = "Devuelto" if prestamo.devuelto else "En préstamo"
            print(f"{prestamo.libro} {estado} desde {prestamo.fecha_prestamo}")