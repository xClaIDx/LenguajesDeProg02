class Nadador:
    def nadar(self):
        return "Nadando en el agua."
    
class Volador:
    def volar(self):
        return "Volando por el Aire."
    
class Pato(Nadador, Volador):
    def Graznar(self):
        return "¡Cuack Cuack!"
    
class Pinguino(Nadador):
    def Graznar(self):
        return "¡Gua Gua!"
    
class Cisne(Nadador, Volador):
    def Graznar(self):
        return "¡Honk Honk!"
    

pato = Pato()
print(f"Pato: {pato.Graznar()}")
print(f"Pato: {pato.nadar()}")
print(f"Pato: {pato.volar()}\n")

pinguino = Pinguino()
print(f"\nPingüino: {pinguino.Graznar()}")
print(f"Pingüino: {pinguino.nadar()}\n")

cisne = Cisne()
print(f"Cisne: {cisne.Graznar()}")
print(f"Cisne: {cisne.nadar()}")
print(f"Cisne: {cisne.volar()}\n")


    
