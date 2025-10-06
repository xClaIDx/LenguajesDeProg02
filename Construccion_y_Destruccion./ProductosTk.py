import tkinter as tk
from tkinter import messagebox
import gc

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"Producto registrado: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")  

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}\n"
    
    def __del__(self):
        print(f"El producto '{self.nombre}' ha sido eliminado.")


class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Inventario")
        self.inventario = []

        # ----- Entradas -----
        tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Precio:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_precio = tk.Entry(root)
        self.entry_precio.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Cantidad:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

        # ----- Botones -----
        tk.Button(root, text="Registrar producto", command=self.registrar).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Mostrar inventario", command=self.mostrar).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Eliminar todos", command=self.eliminar_todos).grid(row=4, column=0, columnspan=2, pady=10)

        # ----- Área de texto -----
        self.text_area = tk.Text(root, width=60, height=12)
        self.text_area.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def registrar(self):
        nombre = self.entry_nombre.get().strip()
        precio = self.entry_precio.get().strip()
        cantidad = self.entry_cantidad.get().strip()

        if not nombre or not precio or not cantidad:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")
            return

        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser número y la cantidad un entero.")
            return

        producto = Producto(nombre, precio, cantidad)
        self.inventario.append(producto)

        messagebox.showinfo("Éxito", f"Producto '{nombre}' registrado.")
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)

    def mostrar(self):
        self.text_area.delete(1.0, tk.END)
        if not self.inventario:
            self.text_area.insert(tk.END, "No hay productos registrados.\n")
        else:
            for producto in self.inventario:
                self.text_area.insert(tk.END, producto.mostrar_informacion())

    def eliminar_todos(self):
        self.inventario.clear()
        gc.collect()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Todos los productos han sido eliminados.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
    print("\nFin programa")