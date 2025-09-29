class Rectangulo:
    def __init__(self,base , altura):
        self.base = base
        self.altura= altura

    def calcularArea(self):
        return self.base * self.altura

rectangulo = Rectangulo(10,5)
area = rectangulo.calcularArea()
print (F"La area del rectangulo es: {area}")
