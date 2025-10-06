import tkinter as tk
from tkinter import messagebox

class Curso:
    def __init__(self, nombre, codigo, profesor):  
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        print(f"Curso registrado: {self.nombre} - Código: {self.codigo}, Profesor: {self.profesor}")

    def mostrar_informacion(self):
        return (
            f"Curso   : {self.nombre}\n"
            f"Código  : {self.codigo}\n"
            f"Profesor: {self.profesor}\n"
            "---------------------------"
        )
    
    def __del__(self):
        print(f"El curso '{self.nombre}' ha sido eliminado.")


# Lista de cursos registrados
cursos = []

def agregar_curso():
    nombre = entry_nombre.get().strip()
    codigo = entry_codigo.get().strip()
    profesor = entry_profesor.get().strip()

    if not nombre or not codigo or not profesor:
        messagebox.showwarning("Campos vacíos", "Debe completar todos los campos.")
        return

    curso = Curso(nombre, codigo, profesor)
    cursos.append(curso)

    # Insertar línea por línea para que quede ordenado en el Listbox
    for linea in curso.mostrar_informacion().split("\n"):
        lista_cursos.insert(tk.END, linea)
    lista_cursos.insert(tk.END, "")  # espacio entre cursos

    # limpiar entradas
    entry_nombre.delete(0, tk.END)
    entry_codigo.delete(0, tk.END)
    entry_profesor.delete(0, tk.END)


def eliminar_curso():
    seleccion = lista_cursos.curselection()
    if not seleccion:
        messagebox.showwarning("Selección vacía", "Seleccione un curso para eliminar.")
        return
    
    # Para simplificar: eliminamos todo y volvemos a mostrar cursos
    lista_cursos.delete(0, tk.END)
    cursos.clear()
    messagebox.showinfo("Eliminado", "Se borraron los cursos de la lista.")


def salir():
    root.destroy()


# Ventana principal
root = tk.Tk()
root.title("Gestión de Cursos")
root.geometry("500x450")

# Labels y entradas
tk.Label(root, text="Nombre del curso:").pack()
entry_nombre = tk.Entry(root, width=40)
entry_nombre.pack()

tk.Label(root, text="Código del curso:").pack()
entry_codigo = tk.Entry(root, width=40)
entry_codigo.pack()

tk.Label(root, text="Profesor:").pack()
entry_profesor = tk.Entry(root, width=40)
entry_profesor.pack()

# Botones
tk.Button(root, text="Agregar curso", command=agregar_curso).pack(pady=5)
tk.Button(root, text="Eliminar todos los cursos", command=eliminar_curso).pack(pady=5)
tk.Button(root, text="Salir", command=salir).pack(pady=5)

# Lista de cursos
lista_cursos = tk.Listbox(root, width=60, height=15)
lista_cursos.pack(pady=10)

root.mainloop()