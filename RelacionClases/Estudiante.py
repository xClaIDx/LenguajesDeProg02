class Estudiante:
    def __init__(self, nombre,dni,codigo_est):
        self.nombre = nombre
        self.dni = dni
        self.codigo_est = codigo_est
        self.cursos = []

    def inscribirse(self, curso):
        self.curso = curso
        curso.agregar_estudiante(self)

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("DNI:", self.dni)
        print("Codigo Estudiante:", self.codigo_est)
        print("Cursos Inscritos:")
        for curso in self.cursos:
            print("-", curso.nombre)

class Profesor:
    def __init__(self,nombre,dni,especialidad):
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("DNI:", self.dni)
        print("Especialidad:", self.especialidad)

class Curso:
    def __init__(self,nombre_curso, profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
        
    def mostrar_detalles(self):
        print("Nombre del Curso:", self.nombre_curso)
        print("Profesor:")
        self.profesor.mostrar_informacion()
        print("Estudiantes Inscritos:")
        for estudiante in self.estudiantes:
            print (f"{estudiante.nombre} {estudiante.codigo_est}")

class Universidad:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        for curso in self.cursos:
            curso.mostrar_detalles()
            print()

prof1 = Profesor("Ing. Juan Carlos","01323043","Programacion")

curso1 = Curso("Lenguajes de Programacion 2",prof1)
curso2 = Curso("Base de Datos",prof1)

est1 = Estudiante("Milena Kelly","01234567","20251001")
est2 = Estudiante("Hennry Quispe Ramos","98765432","20251002")

univ=Universidad("Universidad Nacional Del Altiplano ")

univ.agregar_curso(curso1)
univ.agregar_curso(curso2)

est1.inscribirse(curso1)
est1.inscribirse(curso2)
est2.inscribirse(curso2)   

univ.mostrar_cursos()
est1.mostrar_informacion()
est2.mostrar_informacion()

