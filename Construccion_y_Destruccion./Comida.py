import math

class Comida:
    def __init__(self,proteinas,carbohidratos,grasas):
        self.proteinas=proteinas
        self.carbohidratos=carbohidratos
        self.grasas=grasas
        print("Objeto comida creado \n")
        print(f"{proteinas},{carbohidratos},{grasas} \n")

    def calcular_calorias(self):
        calorias= (self.proteinas * 4) + (self.carbohidratos * 4) + (self.grasas * 9)
        return calorias
    
    
    def mostrar_info(self):

        print ("INFORMACION NUTRICIONAL \n")
        print (f"Proteinas: {self.proteinas}g ")
        print (f"Carbohidratos: {self.carbohidratos}g ")
        print (f"Grasas: {self.grasas}g ")
        print (f"Calorias totales: {self.calcular_calorias()} kcal")

def main():
    
    proteinas = float(input("Ingrese la cantidad de proteinas (g): "))
    carbohidratos = float(input("Ingrese la cantidad de carbohidratos (g): "))
    grasas = float(input("Ingrese la cantidad de grasas (g): "))        

    almuerzo=Comida(proteinas,carbohidratos,grasas)
    almuerzo.mostrar_info()

    del almuerzo

    try:
        print(almuerzo)
    except NameError:
        print("El objeto almuerzo ya no existe.")

if __name__=="__main__":
    main()
