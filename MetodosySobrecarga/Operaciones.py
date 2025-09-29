class Operaciones:
    def Sumar (self,a,b,c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b
miSuma = Operaciones()
resultado1 = miSuma.Sumar(1,0,3)
resultado2 = miSuma.Sumar(1,0)
print (F"{resultado1}")
print (F"{resultado2}")
