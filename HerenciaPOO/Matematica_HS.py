import math

class FiguraGeometrica: # Clase base para figuras geométricas
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
    
    def perimetro(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
    
class Circulo(FiguraGeometrica):# Subclase para círculos
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)
    
    def perimetro(self):
        return math.pi * 2 * self.radio
    
class Rectangulo(FiguraGeometrica): # Subclase para rectángulos
    def __init__(self, ancho, alto):
        super().__init__("Rectángulo")
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    

    
circulo = Circulo(5)              # Crear un objeto de Circulo
print(f"\n{circulo.nombre} con radio {circulo.radio}:")
print(f"Área: {circulo.area()}")
print(f"Perímetro: {circulo.perimetro()}")

rectangulo = Rectangulo(4, 6)     # Crear un objeto de Rectangulo
print(f"\n{rectangulo.nombre} con ancho {rectangulo.ancho} y alto {rectangulo.alto}:")
print(f"Área: {rectangulo.area()}")
print(f"Perímetro: {rectangulo.perimetro()}\n")