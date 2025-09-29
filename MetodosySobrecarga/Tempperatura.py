class Temperatura:
    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

    def ConversionC(self):
        return (self.valor - 32) * 5/9

    def ConversionF(self):
        return (self.valor * 9/5) + 32

valor = float(input("Ingresa el valor de la temperatura: "))
opcion = input("Ingrese si es en Celsius o Farenheit  ").lower()

t = Temperatura(valor)

if opcion == 'f':
    print(f"{t.get_valor()}°F = {t.ConversionC():.2f}°C")
elif opcion == 'c':
    print(f"{t.get_valor()}°C = {t.ConversionF():.2f}°F")
else:
    print("Opción no válida")
