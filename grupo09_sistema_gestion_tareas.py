# Grupo 9
# Miguel Madrigal Murillo
# Carlos Castrillo Rivas

# https://github.com/mamm26/SistemaGestionTareas

import datetime

# Formato [[tarea1, estado], [tarea2, estado]...]
# Indexes: 0: Titulo - 1: Descrip - 2: Fecha - 3: Costo
tareas = []
estados = ["Pendiente", "Completada"]

def divisor():
    print("=======================================")

# Se usa para cambiar las tareas según el ID.    
def mostrarListaTareas():
    if len(tareas) == 0:
        print("NO hay tareas")
        return

    divisor()
    print("Mostrando Tareas:")
    for id, t in enumerate(tareas):

        # Aumentamos 1 dado que el índice inicial es 0.
        id2 = id + 1

        #        Id      Titulo
        print(f"{id2} - {t[0][0]}")

    divisor()

# Verificador de fecha válida
def esFechaValida(fecha):
    try:
        dia, mes, anno = map(int, fecha.split("-"))
        if dia > 31 or mes > 12:
            return False
        
        datetime.datetime(anno, mes, dia)
        return True
    except:
        return False

# Devolvemos la cantidad de tareas pendientes
def cantidadTareasPendientes():
    contar = 0
    for t in tareas:

        # t[1] = Estado de tarea
        # estados[0] = Pendiente
        if t[1] == estados[0]:
            contar += 1
    return contar

def cantidadTareasCompletadas():
    contar = 0
    for t in tareas:

        # t[1] = Estado de tarea
        # estados[1] = Completada
        if t[1] == estados[1]:
            contar += 1
    return contar

# Devuelve el costo de tareas en texto
def costeTareas():

    costoPendientes = 0
    costoCompletadas = 0
    costoTotal = 0

    # Ver informacion Estados, Formato e Indexes
    for t in tareas:
        costoTarea = t[0][3]
        if t[1] == estados[0]: # Pendientes
            costoPendientes += costoTarea # Costo
        elif t[1] == estados[1]: # Completadas
            costoCompletadas += costoTarea

    costoTotal = costoPendientes + costoCompletadas

    return f"- Costo Tareas Pendientes: {costoPendientes}.\n - Costo Tareas Completadas: {costoCompletadas}.\n - Costo TOTAL: {costoTotal}\n"
        
# Menu
menu = "0"
# Sólo sale con la opción 7 (Salir)
menuMax = 7
while menu != str(menuMax):
    print("===== SISTEMA DE GESTIÓN DE TAREAS =====") 
    print("1- Agregar Tarea")
    print("2- Ver Tareas pendientes o completadas")
    print("3- Marcar Tarea como completada")
    print("4- Editar o borrar Tareas")
    print("5- Guardar y Cargar Tareas")
    print("6- Estadísticas Simples")
    print("7- Salir del programa")

    menu = input("Digite la opción: ")

    # Verificamos que exista la opción en el menú
    menuValido = False
    for m in range(menuMax):
        if menu == str(m + 1):
            menuValido = True
            break

    if menuValido == False:
        print(f"¡Error! La opción no es válida. Elige entre 1-{menuMax}.")
        menu = "0"

    # Agregar Tarea
    if menu == "1":

        divisor()
        print("AGREGAR TAREA")
        divisor()
        
        # Solicitamos los datos de la tarea
        titulo = input("Ingrese el Título: ")
        descripcion = input("Ingrese la Descripción: ")
        fecha = input("Ingrese la Fecha (DD-MM-YYYY | Ejemplo: 29-03-2024): ")
        costo = float(input("Ingrese el Costo: "))

        # Verificamos que sea una fecha válida
        while esFechaValida(fecha) == False:
            print("ERROR: Fecha inválida.")
            fecha = input("Ingrese la Fecha (DD-MM-YYYY | Ejemplo: 29-03-2024): ")

        hoy = datetime.datetime.now()
        
        dia, mes, anno = map(int, fecha.split("-"))
        fechaFormato = datetime.datetime(anno, mes, dia)

        while fechaFormato <= hoy:
            print("ERROR: Digite una fecha posterior a hoy.")
            fecha = input("Ingrese la Fecha (DD-MM-YYYY | Ejemplo: 29-03-2024): ")
            dia, mes, anno = map(int, fecha.split("-"))
            fechaFormato = datetime.datetime(anno, mes, dia)

        #       Titulo      Descripcion     Fecha   Costo
        tareaInfo = [titulo,    descripcion,    fechaFormato,  costo]

        #       Tarea Info   Estados -> Pendiente
        tarea = [tareaInfo, estados[0]]
        tareas.append(tarea)
        print(f"CORRECTO: Se ha añadido la tarea '{titulo}'.")
        
    # Ver Tareas pendientes o completadas
    elif menu == "2":
        print("Próximamente...")
    # Marcar Tarea como completada
    elif menu == "3":
        print("Próximamente...")
    # Editar o borrar Tareas
    elif menu == "4":
        print("Próximamente...")
    # Guardar y Cargar Tareas
    elif menu == "5":
        print("Próximamente...")

    # Estadísticas simples
    elif menu == "6":

        divisor()
        print("ESTADÍSTICAS SIMPLES")
        divisor()
        
        totalTareas = len(tareas)

        # TODO: Ordenar tareas por fecha
        print(f"Total de Tareas: {totalTareas}.\n",
              f"Total de Tareas Pendientes: {cantidadTareasPendientes()}.\n",
              f"Total de Tareas Completadas: {cantidadTareasCompletadas()}.\n",
              "============",
              "\nCosto Tareas:\n",
              costeTareas(),
              "============",
              )
    # Salir
    elif menu == str(menuMax):
        print("¡HASTA LUEGO!")

        
    
    
