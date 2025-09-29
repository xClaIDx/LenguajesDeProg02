class IMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def clasificador(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25:
            return "Normal"
        elif imc < 30:
            return "Sobrepeso"
        elif imc < 35:
            return "Obesidad grado I"
        elif imc < 40:
            return "Obesidad grado II"
        else:
            return "Obesidad grado III (mórbida)"

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

persona = IMC(peso, altura)

print(f"Su IMC es: {persona.calcular_imc():.2f}")
print(f"Clasificación: {persona.clasificador()}")
