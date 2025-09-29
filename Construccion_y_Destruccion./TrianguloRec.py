import math

class TrianguloRectangulo:
      def __init__(self,cateto_a,cateto_b):#Constructor
         self.cateto_a=cateto_a
         self.cateto_b=cateto_b

      def calcular_hipotenusa(self):
         hipotenusa = math.sqrt(self.cateto_a**2 + self.cateto_b**2)
         return hipotenusa
      
      def __del__  (self):
         print("Se ha eliminado el objeto TrianguloRectangulo") 
    
def main():
    cateto_a=float(input("Ingrese el valor del cateto a: "))
    cateto_b=float(input("Ingrese el valor del cateto b: "))

    triangulo = TrianguloRectangulo(cateto_a,cateto_b)
    resultado=triangulo.calcular_hipotenusa()
    
    print(F"La hipotenusa del triangulo es : {resultado: .2f}")


if __name__=="__main__":
    main()
