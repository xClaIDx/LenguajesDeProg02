class Peso:
    def __init__(self, peso_kg):
        self.peso_kg = peso_kg

class Altura:
    def __init__(self, altura_m):
        self.altura_m = altura_m

class IMC(Peso, Altura):
    def __init__(self, peso_kg, altura_m):
        Peso.__init__(self, peso_kg)
        Altura.__init__(self, altura_m)

    def calcular_imc(self):
        if self.altura_m <= 0:
            raise ValueError("La altura debe ser mayor que cero.")
        return  self.peso_kg / (self.altura_m ** 2)
    
    def categoria_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc < 24.9:
            return "Normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidad"
        
    def mostrar_resultados(self):
        imc = self.calcular_imc()
        categoria = self.categoria_imc()
        return f"IMC: {imc:.2f}, Categoría: {categoria}"
    
def leer_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un valor positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

peso = leer_float("Ingrese su peso en kilogramos: ")
altura = leer_float("Ingrese su altura en metros: ")

persona= IMC(peso, altura)
print(persona.mostrar_resultados())