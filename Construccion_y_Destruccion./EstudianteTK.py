import tkinter as tk
from tkinter import messagebox
import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"Estudiante registrado: {self.nombre} {self.edad} {self.carrera}")
         
    def mostrar_informacion(self):
        return f"{self.nombre} estudia {self.carrera} y tiene {self.edad} años."
              
    def __del__(self):
        print(f"El estudiante {self.nombre} ha sido eliminado.")


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Estudiantes")
        self.grupo = []

        # Labels y entradas
        tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Edad:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_edad = tk.Entry(root)
        self.entry_edad.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Carrera:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_carrera = tk.Entry(root)
        self.entry_carrera.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        tk.Button(root, text="Registrar", command=self.registrar).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Mostrar Estudiantes", command=self.mostrar).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Eliminar Todos", command=self.eliminar_todos).grid(row=4, column=0, columnspan=2, pady=10)

        # Área de texto para mostrar resultados
        self.text_area = tk.Text(root, width=50, height=12)
        self.text_area.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def registrar(self):
        nombre = self.entry_nombre.get().strip()
        edad = self.entry_edad.get().strip()
        carrera = self.entry_carrera.get().strip()

        if not nombre or not edad or not carrera:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")
            return

        try:
            edad = int(edad)
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        estudiante = Estudiante(nombre, edad, carrera)
        self.grupo.append(estudiante)

        messagebox.showinfo("Éxito", f"Estudiante {nombre} registrado.")
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_carrera.delete(0, tk.END)

    def mostrar(self):
        self.text_area.delete(1.0, tk.END)
        if not self.grupo:
            self.text_area.insert(tk.END, "No hay estudiantes registrados.\n")
        else:
            for est in self.grupo:
                self.text_area.insert(tk.END, est.mostrar_informacion() + "\n")

    def eliminar_todos(self):
        self.grupo.clear()
        gc.collect()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Todos los estudiantes han sido eliminados.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    print("Fin programa")