class Estudiante:
    def __init__(self, nombre, dni, codigo_est):
        self.nombre = nombre
        self.dni = dni
        self.codigo_est = codigo_est
        self.cursos = []  # lista de cursos inscritos

    def inscribirse(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.agregar_estudiante(self)  # relación bidireccional

    def mostrar_informacion(self):
        print(f"\n Estudiante: {self.nombre}")
        print(f"   DNI: {self.dni}")
        print(f"   Código: {self.codigo_est}")
        print("   Cursos Inscritos:")
        if self.cursos:
            for curso in self.cursos:
                print(f"    - {curso.nombre_curso} (Profesor: {curso.profesor.nombre})")
        else:
            print("    Ninguno")


class Profesor:
    def __init__(self, nombre, dni, especialidad):
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print(f" {self.nombre} - {self.especialidad} (DNI: {self.dni})")


class Curso:
    def __init__(self, nombre_curso, profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

    def mostrar_detalles(self):
        print(f"\n Curso: {self.nombre_curso}")
        print("Profesor:")
        self.profesor.mostrar_informacion()
        print("Estudiantes Inscritos:")
        if self.estudiantes:
            for est in self.estudiantes:
                print(f"   - {est.nombre} ({est.codigo_est})")
        else:
            print("   Ninguno")


class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f"\n Universidad: {self.nombre}")
        print("=" * 60)
        for curso in self.cursos:
            curso.mostrar_detalles()
            print("-" * 60)


prof1 = Profesor("Ing. Juan Carlos", "01323043", "Programación")
prof2 = Profesor("Dr. Morillos", "9876543", "Estadística")
prof3 = Profesor("Ing. Percy Lipa", "76451234", "Bases de Datos")

curso1 = Curso("Lenguajes de Programación II", prof1)
curso2 = Curso("Base de Datos", prof3)
curso3 = Curso("Muestreo", prof2)
curso4 = Curso("Programación Numérica", prof1)
curso5 = Curso("Sistemas y Gestión de BD", prof3)
curso6 = Curso("Análisis y Diseño de Sistemas", prof1)
curso7 = Curso("Modelos Discretos", prof2)


est1 = Estudiante("Milena Kelly", "01234567", "20251001")
est2 = Estudiante("Hennry Quispe", "98765432", "20251002")
est3 = Estudiante("Clyde Paricahua", "74321598", "20251003")
est4 = Estudiante("Valeria Mamani", "72345612", "20251004")
est5 = Estudiante("José Apaza", "79865431", "20251005")


univ = Universidad("Universidad Nacional del Altiplano")


for curso in [curso1, curso2, curso3, curso4, curso5, curso6, curso7]:
    univ.agregar_curso(curso)

est1.inscribirse(curso1)
est1.inscribirse(curso2)
est2.inscribirse(curso2)
est2.inscribirse(curso3)
est3.inscribirse(curso1)
est3.inscribirse(curso4)
est3.inscribirse(curso5)
est4.inscribirse(curso6)
est5.inscribirse(curso7)
est5.inscribirse(curso1)

univ.mostrar_cursos()
est1.mostrar_informacion()
est2.mostrar_informacion()
est3.mostrar_informacion()
est4.mostrar_informacion()
est5.mostrar_informacion()