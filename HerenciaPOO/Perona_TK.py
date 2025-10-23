"""
Interfaz Tkinter estilo sci-fi oscuro con almacenamiento de perfiles.
Mejoras:
- Permite guardar y seleccionar perfiles.
- Textos largos hacen salto de línea automático.
- Avatar circular azul con degradado sutil.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ----------------------
# Colores y tipografía
# ----------------------
BG = "#071021"         # fondo general
PANEL = "#0d1824"      # paneles interiores
ACCENT = "#ff7a18"     # acento naranja
ACCENT_DIM = "#c85c12" # acento naranja menos brillante
TEXT = "#e6e6e6"       # texto claro
MUTED = "#9aa6b2"      # texto secundario
HIGHLIGHT = "#132032"  # borde
AVATAR_BLUE = "#1e90ff" # color azul del avatar

DEFAULT_FONT = ("Courier New", 12)
TITLE_FONT = ("Helvetica", 18, "bold")
SMALL_FONT = ("Helvetica", 10)

# ----------------------
# Clases de datos
# ----------------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario

    def trabajar(self):
        return f"Estoy trabajando como {self.profesion} y gano ${self.salario} al mes."

class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad

    def estudiar(self):
        return f"Estudio {self.carrera} en la {self.universidad}."

class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def mostrar_info(self):
        return (f"{self.presentarse()}\n"
                f"{self.trabajar()}\n"
                f"{self.estudiar()}")

# ----------------------
# GUI
# ----------------------
class SciFiUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Panel - Perfil Multirol")
        self.configure(bg=BG)
        self.geometry("880x540")
        self.resizable(False, False)

        self.perfiles = {}  # almacenamiento local de perfiles

        self._build_layout()

    def _build_layout(self):
        header = tk.Frame(self, bg=HIGHLIGHT, height=60)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        tk.Label(header, text="PANEL DE PERFIL", bg=HIGHLIGHT, fg=ACCENT, font=TITLE_FONT).pack(side="left", padx=18)

        main = tk.Frame(self, bg=BG)
        main.pack(fill="both", expand=True, padx=18, pady=18)

        # Panel izquierdo
        left_panel = tk.Frame(main, bg=PANEL, width=360, height=420)
        left_panel.pack(side="left", fill="y", padx=(0,12))
        left_panel.pack_propagate(False)

        tk.Label(left_panel, text="CREAR / EDITAR PERFIL", bg=PANEL, fg=ACCENT, font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(12,8), padx=14)

        self.entries = {}
        fields = [
            ("Nombre", "Juanita"),
            ("Edad", "25"),
            ("Profesión", "Desarrolladora de Software"),
            ("Salario", "2500"),
            ("Carrera", "Ingeniería Estadística e Informática"),
            ("Universidad", "Universidad Nacional del Altiplano"),
        ]

        for label_text, default in fields:
            row = tk.Frame(left_panel, bg=PANEL)
            row.pack(fill="x", pady=6)
            tk.Label(row, text=label_text, width=12, anchor="w", bg=PANEL, fg=MUTED, font=SMALL_FONT).pack(side="left")
            ent = tk.Entry(row, bg=BG, fg=TEXT, insertbackground=TEXT, font=DEFAULT_FONT, relief="flat")
            ent.pack(side="left", fill="x", expand=True, padx=(8,0))
            ent.insert(0, default)
            self.entries[label_text.lower()] = ent

        # Botones principales
        btn_row = tk.Frame(left_panel, bg=PANEL)
        btn_row.pack(fill="x", pady=10, padx=12)

        tk.Button(btn_row, text="Guardar Perfil", bg=ACCENT, fg=BG, relief="flat", command=self._on_guardar, font=DEFAULT_FONT).pack(side="left", padx=(0,8), ipadx=6, ipady=4)
        tk.Button(btn_row, text="Mostrar", bg=ACCENT_DIM, fg=BG, relief="flat", command=self._on_mostrar, font=DEFAULT_FONT).pack(side="left", ipadx=6, ipady=4)

        # Selección de perfil
        tk.Label(left_panel, text="Seleccionar perfil: ", bg=PANEL, fg=MUTED, font=SMALL_FONT).pack(anchor="w", padx=14, pady=(10,0))
        self.combo = ttk.Combobox(left_panel, state="readonly")
        self.combo.pack(fill="x", padx=14, pady=6)
        self.combo.bind("<<ComboboxSelected>>", self._on_seleccionar)

        # Panel derecho: vista
        right_panel = tk.Frame(main, bg=PANEL, width=460, height=420)
        right_panel.pack(side="right", fill="both")
        right_panel.pack_propagate(False)

        self.canvas = tk.Canvas(right_panel, bg=PANEL, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Avatar mejorado (azul)
        cx, cy, r = 120, 110, 65
        self.canvas.create_oval(cx-r-6, cy-r-6, cx+r+6, cy+r+6, fill="#0a2540", outline='')
        self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=AVATAR_BLUE, outline='')
        self.canvas.create_text(cx, cy, text="JD", fill=TEXT, font=("Courier New", 22, "bold"), tags='avatar_text')

        # Textos de perfil
        self._info_title = self.canvas.create_text(260, 70, anchor="w", text="NOMBRE: —", fill=ACCENT, font=("Helvetica", 12, "bold"), width=180)
        self._info_line1 = self.canvas.create_text(260, 100, anchor="w", text="Edad: —", fill=TEXT, font=DEFAULT_FONT, width=180)
        self._info_line2 = self.canvas.create_text(260, 130, anchor="w", text="Profesión: —", fill=TEXT, font=DEFAULT_FONT, width=180)
        self._info_line3 = self.canvas.create_text(260, 160, anchor="w", text="Salario: —", fill=MUTED, font=DEFAULT_FONT, width=180)
        self._info_studies = self.canvas.create_text(40, 220, anchor="w", text="—", fill=TEXT, font=DEFAULT_FONT, width=380)

    def _on_guardar(self):
        nombre = self.entries['nombre'].get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Debe ingresar un nombre para guardar el perfil.")
            return
        datos = {k: v.get() for k, v in self.entries.items()}
        self.perfiles[nombre] = datos
        self.combo['values'] = list(self.perfiles.keys())
        messagebox.showinfo("Guardado", f"Perfil '{nombre}' guardado correctamente.")

    def _on_seleccionar(self, event):
        nombre = self.combo.get()
        datos = self.perfiles.get(nombre, {})
        for k, v in datos.items():
            if k in self.entries:
                self.entries[k].delete(0, tk.END)
                self.entries[k].insert(0, v)
        self._on_mostrar()

    def _on_mostrar(self):
        nombre = self.entries['nombre'].get().strip() or "—"
        edad = self.entries['edad'].get().strip() or "—"
        profesion = self.entries['profesión'].get().strip() or "—"
        salario = self.entries['salario'].get().strip() or "—"
        carrera = self.entries['carrera'].get().strip() or "—"
        universidad = self.entries['universidad'].get().strip() or "—"

        self.canvas.itemconfigure(self._info_title, text=f"NOMBRE: {nombre}")
        self.canvas.itemconfigure(self._info_line1, text=f"Edad: {edad} años")
        self.canvas.itemconfigure(self._info_line2, text=f"Profesión: {profesion}")
        self.canvas.itemconfigure(self._info_line3, text=f"Salario: ${salario}")
        self.canvas.itemconfigure(self._info_studies, text=f"{carrera}\n{universidad}")

        initials = ''.join([p[0] for p in nombre.split() if p]).upper()[:2] or "—"
        self.canvas.delete('avatar_text')
        self.canvas.create_text(120, 110, text=initials, fill=TEXT, font=("Courier New", 22, "bold"), tags='avatar_text')

if __name__ == '__main__':
    app = SciFiUI()
    app.mainloop()