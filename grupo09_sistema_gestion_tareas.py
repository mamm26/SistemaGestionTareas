# Grupo 9
# Miguel Madrigal Murillo
# Carlos Castrillo Rivas
# Erick Vera Meneses


# Menu
# Sólo sale con la opción 6 (Salir)
menu = "0"
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
        print("Próximamente...")
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
    elif menu == "6":
        print("Próximamente...")
    # Salir
    elif menu == str(menuMax):
        print("¡HASTA LUEGO!")

        
    
    
