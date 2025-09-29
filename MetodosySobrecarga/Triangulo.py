class Triangulo:
    def __init__(self, catetoa, catetob):
        self.catetoa = catetoa
        self.catetob = catetob

    def calcularHipotenusa(self):
        return (self.catetoa**2 + self.catetob**2) ** 0.5

    def mostrarInfo(self):
        print(f"La hipotenusa es: {self.calcularHipotenusa():.2f}")

miTriangulo = Triangulo(3, 4)
miTriangulo.mostrarInfo()
