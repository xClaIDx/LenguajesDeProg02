class Producto:
    def __init__ (self,nombre,precio,stock):
        self.nombre= nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre}  -S/.{self.precio:.2f} stock:{self.stock}"

    def __eq__(self,otro):
        return self.nombre==otro.nombre

    def __add__(self,otro):
        return self.precio + otro.precio

    def __gt__(self,otro):
        return self.precio > otro.precio

producto1=Producto("Arroz",3.50, 20)
producto2=Producto("Arroz",3.50,15)
producto3=Producto("Azucar",4.00,10)

print(producto1)
print(producto2)
print(producto3)

print(producto1==producto2)
print(producto1==producto3)

print("La suma de los precios de los poduc.1 y 2 es :",producto1+producto2)
print("La suma de los precios de los poduc.1 y 3 es :",producto1+producto3)

print(producto1 > producto2)
