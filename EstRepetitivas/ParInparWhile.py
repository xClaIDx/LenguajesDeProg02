#Class : CalculadoraSuma
#Atributo: total
#Accion : sumaNumeros
#Objeto : calculadora = Calculadora()
class Calculadora:
    def __init__(self):
        self.total = 0

    def sumaNumeros(self):
        
        print("Calcula la suma de numeros ingresado")
        print("Escribe numeros para sumar . Escribe 'fin' para terminar")

        entrada = ""
        
        while entrada.lower() != "fin":
            entrada = input("Ingrese un numero : ")
            if entrada.isdigit():
                numero =int(entrada)
                self.total += int(entrada)
                if numero == 0:
                    print(f"{numero} es Nulo")
                elif numero % 2 == 0:
                    print(f"{numero} es PAR")
                else:
                    print(f"{numero} es IMPAR")
                
            elif entrada.lower() != "fin":
                print ("Entrada Invalida - Escriba un numero o 'fin' ")
        print(f"a suma total es: {self.total}")
        
def main() :
    calculadora = Calculadora()
    calculadora.sumaNumeros()

if __name__== "__main__":
    main()
