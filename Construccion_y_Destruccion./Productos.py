import gc

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"Producto registrado: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")  

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad} \n" 
    
    def __del__(self):
        print(f"El producto '{self.nombre}' ha sido eliminado.")

inventario = []  # lista de productos

while True:
    agregar = input("¿Desea agregar un producto? (s/n): \n ").strip().lower()
    if agregar == 'n':
        break
    elif agregar == 's':
        nombre = input("Ingrese el nombre del producto: ").strip()
        precio = input("Ingrese el precio del producto: ").strip()
        cantidad = input("Ingrese la cantidad del producto: ").strip()
        try:
            precio = float(precio)
            cantidad = int(cantidad)
            inventario.append((nombre, precio, cantidad))
        except ValueError:
            print("El precio debe ser un número y la cantidad un entero. Intente nuevamente.")
    else:
        print("Opción no válida. Intente nuevamente.")

for dato in inventario:
    producto = Producto(*dato)
    print(producto.mostrar_informacion())

inventario.clear()
del producto
gc.collect()
print("\nFin programa")