class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = 0
        self.precio = precio  

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor > 0:
            self.__precio = valor
        else:
            print("El precio debe ser mayor a 0.")


    def mostrar_producto(self):
        print(f"Producto: {self.__nombre} - Precio: S/ {self.__precio:.2f}")


if __name__ == "__main__":
    nombre = input("Ingrese el nombre del producto: ")
    precio_inicial = float(input("Ingrese el precio del producto: "))

    producto = Producto(nombre, precio_inicial)

    while True:
        print("\nMENÚ PRODUCTO")
        print("1. Mostrar producto")
        print("2. Modificar precio")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto.mostrar_producto()
        elif opcion == "2":
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            producto.precio = nuevo_precio
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")