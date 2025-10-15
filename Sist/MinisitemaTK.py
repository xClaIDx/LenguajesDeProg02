import tkinter as tk
from tkinter import ttk, messagebox

class Profesor:
    def __init__(self, nombre, dni, especialidad):
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad

class Estudiante:
    def __init__(self, nombre, dni, codigo_estudiante):
        self.nombre = nombre
        self.dni = dni
        self.codigo_estudiante = codigo_estudiante
        self.cursos = []

    def inscribirse(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.agregar_estudiante(self)

class Curso:
    def __init__(self, nombre_curso, profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

class SistemaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Universitario - Crying Suns Edition")
        self.root.geometry("900x600")
        self.root.configure(bg="#0a0f1f")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#0a0f1f")
        style.configure("TLabel", background="#0a0f1f", foreground="#c0d6ff", font=("Consolas", 11))
        style.configure("TButton", background="#1a2238", foreground="#c0d6ff", font=("Consolas", 11, "bold"))
        style.map("TButton", background=[('active', '#394867')], foreground=[('active', 'white')])

        self.universidad = Universidad("Universidad Nacional del Altiplano")
        self.profesores = []
        self.estudiantes = []

        title = tk.Label(self.root, text=self.universidad.nombre, fg="#82aaff", bg="#0a0f1f", font=("Consolas", 20, "bold"))
        title.pack(pady=20)

        container = ttk.Notebook(self.root)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        self.tab_profesor = ttk.Frame(container)
        self.tab_curso = ttk.Frame(container)
        self.tab_estudiante = ttk.Frame(container)
        self.tab_mostrar = ttk.Frame(container)

        container.add(self.tab_profesor, text="Registrar Profesor")
        container.add(self.tab_curso, text="Registrar Curso")
        container.add(self.tab_estudiante, text="Registrar Estudiante")
        container.add(self.tab_mostrar, text="Mostrar Datos")

        self.interfaz_profesor()
        self.interfaz_curso()
        self.interfaz_estudiante()
        self.interfaz_mostrar()

    def interfaz_profesor(self):
        frame = ttk.Frame(self.tab_profesor)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(frame, text="DNI:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(frame, text="Especialidad:").grid(row=2, column=0, padx=10, pady=10)

        self.nombre_prof = ttk.Entry(frame, width=30)
        self.dni_prof = ttk.Entry(frame, width=30)
        self.esp_prof = ttk.Entry(frame, width=30)

        self.nombre_prof.grid(row=0, column=1)
        self.dni_prof.grid(row=1, column=1)
        self.esp_prof.grid(row=2, column=1)

        ttk.Button(frame, text="Registrar Profesor", command=self.registrar_profesor).grid(row=3, column=0, columnspan=2, pady=15)

    def interfaz_curso(self):
        frame = ttk.Frame(self.tab_curso)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Nombre del Curso:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(frame, text="Profesor:").grid(row=1, column=0, padx=10, pady=10)

        self.nombre_curso = ttk.Entry(frame, width=30)
        self.nombre_curso.grid(row=0, column=1)

        self.profesor_combo = ttk.Combobox(frame, state="readonly", width=27)
        self.profesor_combo.grid(row=1, column=1)

        ttk.Button(frame, text="Registrar Curso", command=self.registrar_curso).grid(row=2, column=0, columnspan=2, pady=15)

    def interfaz_estudiante(self):
        frame = ttk.Frame(self.tab_estudiante)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(frame, text="DNI:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(frame, text="Código:").grid(row=2, column=0, padx=10, pady=10)
        ttk.Label(frame, text="Curso:").grid(row=3, column=0, padx=10, pady=10)

        self.nombre_est = ttk.Entry(frame, width=30)
        self.dni_est = ttk.Entry(frame, width=30)
        self.cod_est = ttk.Entry(frame, width=30)
        self.curso_combo = ttk.Combobox(frame, state="readonly", width=27)

        self.nombre_est.grid(row=0, column=1)
        self.dni_est.grid(row=1, column=1)
        self.cod_est.grid(row=2, column=1)
        self.curso_combo.grid(row=3, column=1)

        ttk.Button(frame, text="Registrar Estudiante", command=self.registrar_estudiante).grid(row=4, column=0, columnspan=2, pady=15)

    def interfaz_mostrar(self):
        frame = ttk.Frame(self.tab_mostrar)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        self.texto_info = tk.Text(frame, wrap="word", width=80, height=20, bg="#0d152a", fg="#c0d6ff", font=("Consolas", 10))
        self.texto_info.pack(padx=10, pady=10)
        ttk.Button(frame, text="Mostrar Información", command=self.mostrar_datos).pack(pady=10)

    def registrar_profesor(self):
        nombre = self.nombre_prof.get()
        dni = self.dni_prof.get()
        especialidad = self.esp_prof.get()
        if not nombre or not dni or not especialidad:
            messagebox.showwarning("Error", "Complete todos los campos.")
            return
        prof = Profesor(nombre, dni, especialidad)
        self.profesores.append(prof)
        self.actualizar_combobox_profesores()
        messagebox.showinfo("Éxito", f"Profesor {nombre} registrado correctamente.")
        self.nombre_prof.delete(0, tk.END)
        self.dni_prof.delete(0, tk.END)
        self.esp_prof.delete(0, tk.END)

    def registrar_curso(self):
        nombre = self.nombre_curso.get()
        profesor_nombre = self.profesor_combo.get()
        if not nombre or not profesor_nombre:
            messagebox.showwarning("Error", "Complete todos los campos.")
            return
        profesor = next((p for p in self.profesores if p.nombre == profesor_nombre), None)
        curso = Curso(nombre, profesor)
        self.universidad.agregar_curso(curso)
        self.actualizar_combobox_cursos()
        messagebox.showinfo("Éxito", f"Curso {nombre} registrado.")
        self.nombre_curso.delete(0, tk.END)

    def registrar_estudiante(self):
        nombre = self.nombre_est.get()
        dni = self.dni_est.get()
        codigo = self.cod_est.get()
        curso_nombre = self.curso_combo.get()
        if not nombre or not dni or not codigo or not curso_nombre:
            messagebox.showwarning("Error", "Complete todos los campos.")
            return
        curso = next((c for c in self.universidad.cursos if c.nombre_curso == curso_nombre), None)
        est = Estudiante(nombre, dni, codigo)
        est.inscribirse(curso)
        self.estudiantes.append(est)
        messagebox.showinfo("Éxito", f"Estudiante {nombre} registrado e inscrito en {curso_nombre}.")
        self.nombre_est.delete(0, tk.END)
        self.dni_est.delete(0, tk.END)
        self.cod_est.delete(0, tk.END)

    def mostrar_datos(self):
        self.texto_info.delete("1.0", tk.END)
        info = f"Universidad: {self.universidad.nombre}\n\n"
        for curso in self.universidad.cursos:
            info += f"Curso: {curso.nombre_curso}\nProfesor: {curso.profesor.nombre}\n"
            if curso.estudiantes:
                info += "Estudiantes inscritos:\n"
                for est in curso.estudiantes:
                    info += f"   - {est.nombre} ({est.codigo_estudiante})\n"
            else:
                info += "   (Sin estudiantes)\n"
            info += "\n"
        self.texto_info.insert(tk.END, info)

    def actualizar_combobox_profesores(self):
        nombres = [p.nombre for p in self.profesores]
        self.profesor_combo["values"] = nombres

    def actualizar_combobox_cursos(self):
        nombres = [c.nombre_curso for c in self.universidad.cursos]
        self.curso_combo["values"] = nombres

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaApp(root)
    root.mainloop()