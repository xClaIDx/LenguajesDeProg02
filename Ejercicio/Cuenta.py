class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = 0
        self.set_saldo(saldo)

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("El saldo no puede ser negativo.")

    def mostrar_datos(self):
        print(f"Titular: {self.get_titular()} - Saldo : S/ {self.get_saldo():.2f}")


if __name__ == "__main__":
    titular = input("Ingrese el nombre del titular: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))

    cuenta = CuentaBancaria(titular, saldo_inicial)

    if cuenta.get_saldo() == 0 and saldo_inicial < 0:
        print("No se puede crear la cuenta con saldo negativo.")
    else:
        while True:
            print("\nMENÚ CUENTA BANCARIA ")
            print("1. Mostrar datos de la cuenta")
            print("2. Modificar saldo")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cuenta.mostrar_datos()
            elif opcion == "2":
                nuevo_saldo = float(input("Ingrese el nuevo saldo: "))
                cuenta.set_saldo(nuevo_saldo)
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")