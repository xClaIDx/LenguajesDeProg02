class Calculadora:
    def sumar(self,a,b):
        return a,b,a+b

miSuma = Calculadora()
a,b,suma = miSuma.sumar(5,7)

print (F"La Suma de parameros {a} y {b}  es :{suma}")
