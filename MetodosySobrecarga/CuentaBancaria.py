class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def Mostrar(self):
        print(f"Titular: {self.titular} --- Saldo : $ {self.saldo: .2f}")

    def __sub__(self,cantidad):
        if isinstance(cantidad,(int,float)):
            if cantidad <= self.saldo :
                return CuentaBancaria(self.titular,self.saldo-cantidad)
            else:
                print("Fondos insuficientes")
                return self
        else:
            print ("Operador no valido")
            return self
        
titular = input("Ingrese el nombre del titular: ")
saldo = float(input("Ingrese el saldo :"))        

cuenta1 = CuentaBancaria(titular,saldo)
cuenta1.Mostrar()

cuenta2 = cuenta1 - 250
cuenta2.Mostrar()
        
cuenta3 = cuenta2 - 700
cuenta3.Mostrar()
        
