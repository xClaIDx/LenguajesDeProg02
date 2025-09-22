class Numeros:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.contador = 0

    def generarSerie(self):
        print("Números hasta", self.cantidad)
        while self.contador <= self.cantidad:
            print(self.contador, end=" --> ")
            self.contador += 1

def main():
    miNumero = Numeros(10)
    miNumero.generarSerie()

if __name__ == "__main__":
    main()
