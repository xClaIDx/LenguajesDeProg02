import tkinter as tk

class TorresDeHanoi:
    def __init__(self, num_discos, canvas):
        self.num_discos = num_discos
        self.torres = [list(range(num_discos, 0, -1)), [], []]
        self.canvas = canvas
        self.ancho_torre = 20
        self.ancho_disco = 30
        self.alto_disco = 20
        self.margen = 100
        self.posiciones_torres = [
            self.margen,
            self.canvas.winfo_width() // 2,
            self.canvas.winfo_width() - self.margen
        ]
        self.init_grafico()

    def init_grafico(self):
        self.canvas.delete("all")
        for i, x in enumerate(self.posiciones_torres):
            self.canvas.create_rectangle(
                x - self.ancho_torre//2,
                self.canvas.winfo_height() - (self.num_discos + 1) * self.alto_disco,
                x + self.ancho_torre//2,
                self.canvas.winfo_height(),
                fill="brown"
            )
            self.canvas.create_text(x, self.canvas.winfo_height() - 10, text=str(i+1), font=("Arial", 14))
        self.actualizar_grafico()

    def dibujar_disco(self, disco, torre, nivel):
        x = self.posiciones_torres[torre]
        y = self.canvas.winfo_height() - (nivel + 1) * self.alto_disco
        ancho = self.ancho_disco + disco * 10
        color = f"#{(disco*40)%256:02x}{(100 + disco*20)%256:02x}{(200 - disco*20)%256:02x}"
        self.canvas.create_rectangle(
            x - ancho//2, y - self.alto_disco, x + ancho//2, y,
            fill=color, outline="black"
        )

    def actualizar_grafico(self):
        self.canvas.delete("all")
        for i, x in enumerate(self.posiciones_torres):
            self.canvas.create_rectangle(
                x - self.ancho_torre//2,
                self.canvas.winfo_height() - (self.num_discos + 1) * self.alto_disco,
                x + self.ancho_torre//2,
                self.canvas.winfo_height(),
                fill="brown"
            )
            self.canvas.create_text(x, self.canvas.winfo_height() - 10, text=str(i+1), font=("Arial", 14))
        for torre_index, torre in enumerate(self.torres):
            for nivel, disco in enumerate(torre):
                self.dibujar_disco(disco, torre_index, nivel)
        self.canvas.update()

    def mover_disco(self, origen, destino):
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.actualizar_grafico()
        input(f"Mover disco {disco} de Torre {origen+1} a Torre {destino+1}. Presione Enter para continuar...")

    def resolver(self, n=None, origen=0, destino=2, auxiliar=1):
        if n is None:
            n = self.num_discos
        if n == 1:
            self.mover_disco(origen, destino)
        else:
            self.resolver(n-1, origen, auxiliar, destino)
            self.mover_disco(origen, destino)
            self.resolver(n-1, auxiliar, destino, origen)


if __name__ == "__main__":
    num_discos = 4
    root = tk.Tk()
    root.title("Torres de Hanoi")
    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()
    root.update()

    juego = TorresDeHanoi(num_discos, canvas)
    input("Presione Enter para iniciar la animación")
    juego.resolver()
    print("¡Problema resuelto!")
    root.mainloop()