import tkinter as tk
from tkinter import messagebox
import gc

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro registrado: {self.titulo} de {self.autor}, {self.anio}")
         
    def mostrar_informacion(self):
        return f"'{self.titulo}' fue escrito por {self.autor} en el año {self.anio}."
              
    def __del__(self):
        print(f"El libro '{self.titulo}' ha sido eliminado.")


class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Biblioteca")
        self.biblioteca = []

        # ----- Entradas -----
        tk.Label(root, text="Título:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_titulo = tk.Entry(root)
        self.entry_titulo.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Autor:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_autor = tk.Entry(root)
        self.entry_autor.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Año:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_anio = tk.Entry(root)
        self.entry_anio.grid(row=2, column=1, padx=5, pady=5)

        # ----- Botones -----
        tk.Button(root, text="Registrar libro", command=self.registrar).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Mostrar libros", command=self.mostrar).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Eliminar todos", command=self.eliminar_todos).grid(row=4, column=0, columnspan=2, pady=10)

        # ----- Área de texto -----
        self.text_area = tk.Text(root, width=60, height=12)
        self.text_area.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def registrar(self):
        titulo = self.entry_titulo.get().strip()
        autor = self.entry_autor.get().strip()
        anio = self.entry_anio.get().strip()

        if not titulo or not autor or not anio:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")
            return

        try:
            anio = int(anio)
        except ValueError:
            messagebox.showerror("Error", "El año debe ser un número entero.")
            return

        libro = Libro(titulo, autor, anio)
        self.biblioteca.append(libro)

        messagebox.showinfo("Éxito", f"Libro '{titulo}' registrado.")
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_anio.delete(0, tk.END)

    def mostrar(self):
        self.text_area.delete(1.0, tk.END)
        if not self.biblioteca:
            self.text_area.insert(tk.END, "No hay libros registrados.\n")
        else:
            for libro in self.biblioteca:
                self.text_area.insert(tk.END, libro.mostrar_informacion() + "\n")

    def eliminar_todos(self):
        self.biblioteca.clear()
        gc.collect()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Todos los libros han sido eliminados.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
    print("\nFin programa")