#Class : CalculadoraRango
#Atributo: total
#Accion : ingresarNumeros
#Objeto : calculadora = CalcularRango()

class CalcularRango:
    def __init__(self):
        self.total = 0

    def ingresarNumeros(self):
        print("Calculadora de números entre 1 y 10")
        print("Escribe números para sumar. Escribe 'fin' para terminar")

        entrada = ""
        while entrada.lower() != "fin":
            entrada = input("Ingrese un número (1-10): ")

            if entrada.isdigit():
                numero = int(entrada)
                if 0 <= numero <= 10:
                    self.total += numero
                    print(f"{numero} aceptado")
                else:
                    print("Número inválido (debe estar entre 0 y 10)")
            elif entrada.lower() != "fin":
                print("Entrada inválida - Escriba un número entre 0 y 10 o 'fin'")

        print(f"La suma total es: {self.total}")

def main():
    calculadora = CalcularRango()
    calculadora.ingresarNumeros()

if __name__ == "__main__":
    main()
