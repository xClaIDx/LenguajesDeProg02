class VehiculoTerrestre:
    def conducir(self):
        return "Conduciendo por la carretera."  
    def frenar(self):
        return "Frenando el vehículo terrestre se ha detenido."
    
class VehiculoAcuatico:
    def navegar(self):
        return "Navegando por el agua."  
    def fondear(self):
        return "Anclando el vehículo acuático ha fondeado."
    
class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    def transformar(self, modo):
        if modo == "terrestre":
            return "Transformando a modo terrestre."
        elif modo == "acuatico":
            return "Transformando a modo acuático."
        else:
            return "Modo desconocido. Use 'terrestre' o 'acuatico'."
        

def main():
    anfibio = VehiculoAnfibio()
    print(anfibio.transformar("terrestre"))
    print(anfibio.conducir())
    print(anfibio.frenar())

    print("---\n")

    print(anfibio.transformar("acuatico"))
    print(anfibio.navegar())
    print(anfibio.fondear())

if __name__ == "__main__":
    main()