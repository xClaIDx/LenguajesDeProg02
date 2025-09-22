class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)  
        print("Tarea agregada")

    def mostrarTareas(self):
        if not self.tareas:
            print("No hay tareas pendientes")
        else:
            print("Tareas pendientes")
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")  

miGestor = GestorTareas()

while True:
    print("\n---- MENU ----")
    print("1 : Agregar Tarea")
    print("2 : Mostrar Tareas")
    print("3 : Salir")
    opcion = input("Seleccione una opcion: \n")

    if opcion == "1":
        tarea = input("Escribe la tarea: \n")
        miGestor.agregar_tarea(tarea)   
    elif opcion == "2":
        miGestor.mostrarTareas()        
    elif opcion == "3":
        print("Saliendo del gestor de tareas \n")
        break
    else:
        print("Opcion no valida. Intente de nuevo. \n ")

    
