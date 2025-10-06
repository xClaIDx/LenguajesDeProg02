class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = []

    def agregar_departamento(self, departamento):
        self.departamento.append(departamento)

dep1 = Departamento("Ingenieria Estadistica")
dep2 = Departamento("Informatica")

uni = Universidad("UNAP",[])
uni.agregar_departamento(dep1)
uni.agregar_departamento(dep2)
print (uni.departamento[0].nombre)
print (uni.departamento[1].nombre)