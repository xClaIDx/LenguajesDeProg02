import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def __del__(self):
        print("El objeto Circulo ha sido eliminado.")

def main():
    radio = float(input("Ingrese el valor del radio: "))
    circulo = Circulo(radio)
    resultado = circulo.calcular_area()
    print(f"El área del círculo es: {resultado:.2f}")
    
    del circulo

    try:
        #circulo.calcular_area()
        print(circulo)
    except NameError:
        print("El objeto circulo ya no existe.")
        
if __name__ == "__main__":
    main()
