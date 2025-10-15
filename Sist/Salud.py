class Paciente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

class Cita:
    def __init__(self, paciente,fecha,especialidad):
        self.paciente = paciente
        self.fecha = fecha
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print(f"Cita para {self.paciente.nombre} (DNI: {self.paciente.dni}) el {self.fecha} en la especialidad de {self.especialidad}")

class Consultorio:
    def __init__(self):
        self.citas = []

    def agendar_cita(self,nombre,dni,fecha,especialidad):
        paciente = Paciente(nombre,dni)
        cita = Cita(paciente,fecha,especialidad)
        self.citas.append(cita)
        print(f"Cita agendada para {nombre} el {fecha} en la especialidad de {especialidad}")

    def mostrar_citas(self):
        if not self.citas:
            print("No hay citas agendadas")
        else:
            print("\n Lista de Citas Agendadas:")
            for cita in self.citas:
                cita.mostrar_informacion()

    def cancelar_cita(self,dni,fecha):
        for cita in self.citas:
            if cita.paciente.dni == dni and cita.fecha == fecha:
                self.citas.remove(cita)
                print(f"Cita para {cita.paciente.nombre} el {fecha} ha sido cancelada")
                return
        print("No se encontró la cita para cancelar")
        
consultorio = Consultorio()

while True:
    print("\n=== Menu de Consultorio Médico ===")
    print("1. Agendar Cita")
    print("2. Mostrar Citas")
    print("3. Cancelar Cita")
    print("4. Salir")

    opcion = input("Seleccione una opción : ")
    if opcion == '1':
        nombre = input("Ingrese el nombre del paciente: ")
        dni = input("Ingrese el DNI del paciente: ")
        fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")
        especialidad = input("Ingrese la especialidad médica: ")
        consultorio.agendar_cita(nombre,dni,fecha,especialidad)
    elif opcion == '2':
        consultorio.mostrar_citas()
    elif opcion == '3':
        dni = input("Ingrese el DNI del paciente para cancelar la cita: ")
        fecha = input("Ingrese la fecha de la cita a cancelar (DD/MM/AAAA): ")
        consultorio.cancelar_cita(dni,fecha)
    elif opcion == '4':
        print("Saliendo del sistema de consultorio médico.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")