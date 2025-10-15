class Factorial:
    def __init__(self, numero):
        self.__numero = None
        self.set_numero(numero)

    def set_numero(self, numero):
        if isinstance(numero, int) and numero >= 0:
            self.__numero = numero
        else:
            raise ValueError("El número debe ser un entero positivo o cero.")

    def get_numero(self):
        return self.__numero

    def calcular(self):
        resultado = 1
        for i in range(2, self.__numero + 1):
            resultado *= i
        return resultado

    def mostrar_resultado(self):
        print(f"El factorial de {self.get_numero()} es: {self.calcular()}")


if __name__ == "__main__":
    numero = int(input("Ingrese un número para calcular su factorial: "))
    f = Factorial(numero)
    f.mostrar_resultado()