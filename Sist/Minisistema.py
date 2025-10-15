class Profesor:
    def __init__(self, nombre, dni, especialidad):
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad
        print(f"Profesor registrado: {self.nombre}  |  DNI: {self.dni}  |  Especialidad: {self.especialidad}")

    def mostrar_info(self):
        print(f"Profesor: {self.nombre}  |  DNI: {self.dni}  |  Especialidad: {self.especialidad}")


class Estudiante:
    def __init__(self, nombre, dni, codigo_estudiante):
        self.nombre = nombre
        self.dni = dni
        self.codigo_estudiante = codigo_estudiante
        self.cursos = []
        print(f"Estudiante creado: {self.nombre}  |  Código: {self.codigo_estudiante}")

    def inscribirse(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.agregar_estudiante(self)
            print(f"{self.nombre} se inscribió en el curso: {curso.nombre_curso}")
        else:
            print(f"{self.nombre} ya está inscrito en el curso {curso.nombre_curso}")

    def mostrar_info(self):
        print("\n--- Información del Estudiante ---")
        print(f"Nombre     : {self.nombre}")
        print(f"DNI        : {self.dni}")
        print(f"Código     : {self.codigo_estudiante}")
        if self.cursos:
            print("Cursos inscritos:")
            for curso in self.cursos:
                print(f"   - {curso.nombre_curso}")
        else:
            print("   (Sin cursos inscritos)")


class Curso:
    def __init__(self, nombre_curso, profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []
        print(f"Curso registrado: {self.nombre_curso}  |  Profesor: {self.profesor.nombre}")

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

    def mostrar_detalles(self):
        print("\n=== Detalles del Curso ===")
        print(f"Curso     : {self.nombre_curso}")
        print(f"Profesor  : {self.profesor.nombre}")
        print("Estudiantes inscritos:")
        if self.estudiantes:
            for est in self.estudiantes:
                print(f"   - {est.nombre} ({est.codigo_estudiante})")
        else:
            print("   (Sin estudiantes aún)")


class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []
        print(f"\nUniversidad creada: {self.nombre}")

    def agregar_curso(self, curso):
        self.cursos.append(curso)
        print(f"Curso agregado a la universidad: {curso.nombre_curso}")

    def mostrar_cursos(self):
        print("\n=== Cursos de la Universidad ===")
        print(f"Universidad: {self.nombre}")
        if not self.cursos:
            print("   (No hay cursos registrados)")
        else:
            for curso in self.cursos:
                print(f"   - {curso.nombre_curso} (Profesor: {curso.profesor.nombre})")


if __name__ == "__main__":
    prof1 = Profesor("Dr. Morillos", "78965412", "Muestreo")

    curso1 = Curso("Muestreo", prof1)

    est1 = Estudiante("Clyde Paricahua", "74055719", "241419")
    est2 = Estudiante("María Condori", "78541236", "242500")

    est1.inscribirse(curso1)
    est2.inscribirse(curso1)

    unap = Universidad("Universidad Nacional del Altiplano")
    unap.agregar_curso(curso1)

    unap.mostrar_cursos()
    curso1.mostrar_detalles()
    est1.mostrar_info()