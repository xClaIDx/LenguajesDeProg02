class Empleado:
    def __init__ (self,nombre,salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    def salarioAnual (self):
        SalarioFinal = salario_mensual * 12
        return SalarioFinal
    

nombre = input("Ingrese nombre del Empleado")
salario_mensual = int(input("Ingrese salario "))
empleado1 = Empleado(nombre,salario_mensual)
resultado = empleado1.salarioAnual()
print(f"Salario Anual del empleado {nombre} es : {resultado}")

del salario_mensual

try:
    print(salario_mensual)
except:
    print(f"Empleado {nombre} ha sido dado de baja")
    
