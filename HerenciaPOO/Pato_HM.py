class Nadador: # Clase para habilidades de natación
    def nadar(self):
        return "Nadando en el agua."
    
class Volador: # Clase para habilidades de vuelo
    def volar(self):
        return "Volando por el Aire."
    
class Pato(Nadador, Volador):# Subclase que hereda de Nadador y Volador
    def Graznar(self):
        return "¡Cuack Cuack!"
    
class Pinguino(Nadador):# Subclase que solo hereda de Nadador
    def Graznar(self):
        return "¡Gua Gua!"
    
class Cisne(Nadador, Volador):# Subclase que hereda de Nadador y Volador
    def Graznar(self):
        return "¡Honk Honk!"
    

pato = Pato()# Crear un objeto de Pato
print(f"Pato: {pato.Graznar()}")
print(f"Pato: {pato.nadar()}")
print(f"Pato: {pato.volar()}\n")

pinguino = Pinguino()# Crear un objeto de Pinguino
print(f"Pingüino: {pinguino.Graznar()}")
print(f"Pingüino: {pinguino.nadar()}\n")

cisne = Cisne()# Crear un objeto de Cisne
print(f"Cisne: {cisne.Graznar()}")
print(f"Cisne: {cisne.nadar()}")
print(f"Cisne: {cisne.volar()}\n")


    
