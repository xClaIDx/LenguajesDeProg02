import tkinter as tk
from tkinter import ttk

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True


class Prestamo:
    def __init__(self, libro, fecha):
        self.libro = libro
        self.fecha = fecha
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
            self.prestamos.append(Prestamo(libro, fecha))
            return f"✅ Préstamo registrado: {libro.titulo} ({fecha})"
        else:
            return f"⚠️ El libro '{libro.titulo}' no está disponible."

    def mostrar_prestamos(self):
        return [(p.libro.titulo, p.fecha, "Devuelto" if p.devuelto else "Pendiente") for p in self.prestamos]


# ---------------- INTERFAZ TKINTER ----------------

class LibreriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Librería")
        self.root.geometry("800x550")
        self.root.config(bg="black")

        self.libros = []
        self.usuarios = []
        self.mensaje = tk.StringVar(value="Bienvenido al Sistema de Librería Galáctico 📚")

        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure("TFrame", background="black")
        self.estilo.configure("TLabel", background="black", foreground="#00BFFF", font=("Consolas", 12))
        self.estilo.configure("TButton", background="#00BFFF", foreground="white", font=("Consolas", 11, "bold"))
        self.estilo.map("TButton", background=[("active", "#1E90FF")])
        self.estilo.configure("Treeview", background="black", foreground="white", fieldbackground="black", font=("Consolas", 11))
        self.estilo.configure("Treeview.Heading", background="#0A0A0A", foreground="#00BFFF", font=("Consolas", 11, "bold"))

        self.frame_menu()

    def limpiar_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_mensaje(self, texto):
        self.mensaje.set(texto)

    def frame_menu(self):
        self.limpiar_frame()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True)

        ttk.Label(frame, text=" SISTEMA DE LIBRERÍA ", font=("Consolas", 16, "bold")).pack(pady=20)

        ttk.Button(frame, text="➕ Registrar Libro", command=self.frame_registrar_libro).pack(pady=8)
        ttk.Button(frame, text="👤 Registrar Usuario", command=self.frame_registrar_usuario).pack(pady=8)
        ttk.Button(frame, text="📚 Realizar Préstamo", command=self.frame_prestamo).pack(pady=8)
        ttk.Button(frame, text="🧾 Ver Préstamos", command=self.frame_ver_prestamos).pack(pady=8)
        ttk.Button(frame, text="🧨 Borrar Todos los Registros", command=self.borrar_todo).pack(pady=8)
        ttk.Button(frame, text="🚪 Salir", command=self.root.quit).pack(pady=8)

        ttk.Label(self.root, textvariable=self.mensaje, foreground="white", background="black",
                  font=("Consolas", 11, "italic")).pack(side="bottom", pady=10)

    def frame_registrar_libro(self):
        self.limpiar_frame()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True)

        ttk.Label(frame, text="REGISTRAR LIBRO").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Título:").grid(row=1, column=0, sticky="e")
        titulo = tk.Entry(frame, bg="black", fg="white", insertbackground="white")
        titulo.grid(row=1, column=1)

        ttk.Label(frame, text="Autor:").grid(row=2, column=0, sticky="e")
        autor = tk.Entry(frame, bg="black", fg="white", insertbackground="white")
        autor.grid(row=2, column=1)

        ttk.Label(frame, text="ISBN:").grid(row=3, column=0, sticky="e")
        isbn = tk.Entry(frame, bg="black", fg="white", insertbackground="white")
        isbn.grid(row=3, column=1)

        def guardar():
            if titulo.get() and autor.get() and isbn.get():
                self.libros.append(Libro(titulo.get(), autor.get(), isbn.get()))
                self.mostrar_mensaje("✅ Libro registrado correctamente.")
                self.frame_menu()
            else:
                self.mostrar_mensaje("⚠️ Complete todos los campos para registrar el libro.")

        ttk.Button(frame, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="Volver", command=self.frame_menu).grid(row=5, column=0, columnspan=2)

        ttk.Label(self.root, textvariable=self.mensaje, foreground="white", background="black",
                  font=("Consolas", 11, "italic")).pack(side="bottom", pady=10)

    def frame_registrar_usuario(self):
        self.limpiar_frame()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True)

        ttk.Label(frame, text="REGISTRAR USUARIO").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky="e")
        nombre = tk.Entry(frame, bg="black", fg="white", insertbackground="white")
        nombre.grid(row=1, column=1)

        ttk.Label(frame, text="ID Usuario:").grid(row=2, column=0, sticky="e")
        idu = tk.Entry(frame, bg="black", fg="white", insertbackground="white")
        idu.grid(row=2, column=1)

        def guardar():
            if nombre.get() and idu.get():
                self.usuarios.append(Usuario(nombre.get(), idu.get()))
                self.mostrar_mensaje("✅ Usuario registrado correctamente.")
                self.frame_menu()
            else:
                self.mostrar_mensaje("⚠️ Complete todos los campos para registrar el usuario.")

        ttk.Button(frame, text="Guardar", command=guardar).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="Volver", command=self.frame_menu).grid(row=4, column=0, columnspan=2)

        ttk.Label(self.root, textvariable=self.mensaje, foreground="white", background="black",
                  font=("Consolas", 11, "italic")).pack(side="bottom", pady=10)

    def frame_prestamo(self):
        self.limpiar_frame()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True)

        if not self.libros or not self.usuarios:
            self.mostrar_mensaje("⚠️ Debe haber al menos un libro y un usuario registrados.")
            self.frame_menu()
            return

        ttk.Label(frame, text="REALIZAR PRÉSTAMO").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Usuario:").grid(row=1, column=0, sticky="e")
        usuario_var = tk.StringVar()
        usuario_cb = ttk.Combobox(frame, textvariable=usuario_var, values=[u.nombre for u in self.usuarios])
        usuario_cb.grid(row=1, column=1)

        ttk.Label(frame, text="Libro:").grid(row=2, column=0, sticky="e")
        libro_var = tk.StringVar()
        libro_cb = ttk.Combobox(frame, textvariable=libro_var, values=[l.titulo for l in self.libros if l.disponible])
        libro_cb.grid(row=2, column=1)

        ttk.Label(frame, text="Fecha (AAAA-MM-DD):").grid(row=3, column=0, sticky="e")
        fecha = tk.Entry(frame, bg="black", fg="white", insertbackground="white")
        fecha.grid(row=3, column=1)

        def guardar():
            usuario = next((u for u in self.usuarios if u.nombre == usuario_var.get()), None)
            libro = next((l for l in self.libros if l.titulo == libro_var.get()), None)
            if usuario and libro:
                msg = usuario.realizar_prestamo(libro, fecha.get())
                self.mostrar_mensaje(msg)
                self.frame_menu()
            else:
                self.mostrar_mensaje("⚠️ Seleccione un usuario y un libro válidos.")

        ttk.Button(frame, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="Volver", command=self.frame_menu).grid(row=5, column=0, columnspan=2)

        ttk.Label(self.root, textvariable=self.mensaje, foreground="white", background="black",
                  font=("Consolas", 11, "italic")).pack(side="bottom", pady=10)

    def frame_ver_prestamos(self):
        self.limpiar_frame()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True)

        ttk.Label(frame, text="LISTA DE PRÉSTAMOS").pack(pady=10)

        tree = ttk.Treeview(frame, columns=("Usuario", "Libro", "Fecha", "Estado"), show="headings", height=10)
        tree.heading("Usuario", text="Usuario")
        tree.heading("Libro", text="Libro")
        tree.heading("Fecha", text="Fecha")
        tree.heading("Estado", text="Estado")
        tree.pack(expand=True, fill="both")

        for u in self.usuarios:
            for p in u.prestamos:
                tree.insert("", "end", values=(u.nombre, p.libro.titulo, p.fecha, "Devuelto" if p.devuelto else "Pendiente"))

        def marcar_devolucion():
            item = tree.selection()
            if item:
                valores = tree.item(item, "values")
                usuario = next((u for u in self.usuarios if u.nombre == valores[0]), None)
                if usuario:
                    prestamo = next((p for p in usuario.prestamos if p.libro.titulo == valores[1]), None)
                    if prestamo and not prestamo.devuelto:
                        prestamo.marcar_devolucion()
                        self.mostrar_mensaje(f"✅ Libro '{prestamo.libro.titulo}' devuelto correctamente.")
                        self.frame_ver_prestamos()
                    else:
                        self.mostrar_mensaje("⚠️ Este préstamo ya está devuelto.")
            else:
                self.mostrar_mensaje("⚠️ Seleccione un préstamo para marcar como devuelto.")

        ttk.Button(frame, text="Marcar como Devuelto", command=marcar_devolucion).pack(pady=10)
        ttk.Button(frame, text="Volver", command=self.frame_menu).pack(pady=5)

        ttk.Label(self.root, textvariable=self.mensaje, foreground="white", background="black",
                  font=("Consolas", 11, "italic")).pack(side="bottom", pady=10)

    def borrar_todo(self):
        self.libros.clear()
        self.usuarios.clear()
        self.mostrar_mensaje("🧨 Todos los registros han sido eliminados.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibreriaApp(root)
    root.mainloop()