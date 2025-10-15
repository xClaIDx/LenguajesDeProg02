class TorresDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.torres = [list(range(num_discos, 0, -1)), [], []]

    def mover_disco(self, origen, destino):
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.mostrar_estado()
        input("\nPresione Enter para continuar...\n")

    def resolver(self, n=None, origen=0, destino=2, auxiliar=1):
        if n is None:
            n = self.num_discos
        if n == 1:
            print(f"Mover disco 1 de Torre {origen + 1} a Torre {destino + 1}")
            self.mover_disco(origen, destino)
        else:
            self.resolver(n - 1, origen, auxiliar, destino)
            print(f"Mover disco {n} de Torre {origen + 1} a Torre {destino + 1}")
            self.mover_disco(origen, destino)
            self.resolver(n - 1, auxiliar, destino, origen)

    def mostrar_estado(self):
        print("\nEstado de las torres:")
        for i, torre in enumerate(self.torres):
            print(f"Torre {i + 1}: {torre}")


if __name__ == "__main__":
    num_discos = int(input("Ingrese el número de discos: "))
    juego = TorresDeHanoi(num_discos)
    print("Estado inicial:")
    juego.mostrar_estado()
    input("\nPresione Enter para comenzar la resolución...\n")
    juego.resolver()
    print("\n¡Problema resuelto!")