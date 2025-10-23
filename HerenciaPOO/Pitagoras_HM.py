class Catetoa:
    def __init__(self, cateto_a):
        self.cateto_a = cateto_a

class Catetob:
    def __init__(self, cateto_b):
        self.cateto_b = cateto_b

class Hipotenusa(Catetoa, Catetob):
    def __init__(self, cateto_a, cateto_b):
        Catetoa.__init__(self, cateto_a)
        Catetob.__init__(self, cateto_b)


    def calcular_Hipotenusa(self):
        return (self.cateto_a ** 2 + self.cateto_b ** 2) ** 0.5
        
    def mostrar_resultados(self):
        hipotenusa = self.calcular_Hipotenusa()
        return f"Hipotenusa: {hipotenusa:.2f}"
    
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

catetoa = leer_float("Ingrese la longitud del cateto a: ")
catetob = leer_float("Ingrese la longitud del cateto b: ")

hipotenusa = Hipotenusa(catetoa, catetob)
print(hipotenusa.mostrar_resultados())