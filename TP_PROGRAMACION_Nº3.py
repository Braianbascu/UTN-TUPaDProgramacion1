# EJERCICIO Nº3

# # Variables utilizadas
operador = ""
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

print("---SISTEMA CENTRAL CLINICA---")
print("")

while True:
    operador = input("ingrese el nombre del operador: ")

    if operador == "":
        print("Debe ingresar un nombre para continuar")
    elif operador.isalpha():
        print("")
        break
    else:
        print("El nombre debe contener solo letras")

print(f"Bienvenido {operador}")
# menu de seleccion
while True:
    print("-----MENU-----")
    print("")
    print("1- RESERVAR TURNO")
    print("2- CANCELAR TURNO")
    print("3- VER AGENDA DEL DIA")
    print("4- VER RESUMEN GENERAL")
    print("5- SALIR")
    print("")

    opcion = input("Ingrese una opcion: ")
    # Control input ingresado
    if opcion == "":
        print("Debe ingresar una opcion para continuar")
        print("")
    elif not opcion.isdigit():
        print("Ingrese un valor numerico")
        print("")
    else:
        opcion = int(opcion)
        if opcion < 1 or opcion > 5:
            print("Error opcion fuera de rango")
        # Flujo de menu

        # OPCION 1
        elif opcion == 1:
            while True:
                print("1- LUNES")
                print("2- MARTES")
                dia = input("Selecione un dia:")

                if dia == "":
                    print("Debe ingresar una opcion para continuar")
                    print("")
                elif not dia.isdigit():
                    print("Ingrese un valor numerico")
                    print("")
                else:
                    dia = int(dia)

                    if dia < 1 or dia > 2:
                        print("Error opcion fuera de rango")
                    else:
                        break

            while True:
                paciente = input("Por favor ingrese el nombre del paciente: ")

                if paciente == "":
                    print("Debe ingresar un nombre para continuar")
                elif paciente.isalpha():
                    print("")
                    break
                else:
                    print("Debe ingresar solo letras")
            # Verificacion y asignacion de turno
            if dia == 1:
                if (
                    paciente == lunes1
                    or paciente == lunes2
                    or paciente == lunes3
                    or paciente == lunes4
                ):
                    print("El paciente ya tiene u turno asignado")
                elif lunes1 == "":
                    lunes1 = paciente
                    print("paciente asignado al turno 1")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("paciente asignado al turno 2")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("paciente asignado al turno 3")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("paciente asignado al turno 4")
                else:
                    print("No hay turnos disponibles este dia")
            else:
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("El paciente ya tiene u turno asignado")
                elif martes1 == "":
                    martes1 = paciente
                    print("paciente asignado al turno 1")
                elif martes2 == "":
                    martes2 = paciente
                    print("paciente asignado al turno 2")
                elif martes3 == "":
                    martes3 = paciente
                    print("paciente asignado al turno 3")
                else:
                    print("No hay turnos disponibles este dia")
        # OPCION 2
        elif opcion == 2:
            while True:
                print("1- LUNES")
                print("2- MARTES")
                dia = input("Selecione un dia:")

                if dia == "":
                    print("Debe ingresar una opcion para continuar")
                    print("")
                elif not dia.isdigit():
                    print("Ingrese un valor numerico")
                    print("")
                else:
                    dia = int(dia)

                    if dia < 1 or dia > 2:
                        print("Error opcion fuera de rango")
                    else:
                        break
            # Verificacion y cancelacion de turno
            while True:
                paciente = input("Por favor ingrese el nombre del paciente: ")

                if paciente == "":
                    print("Debe ingresar un nombre para continuar")
                elif paciente.isalpha():
                    print("")
                    break
                else:
                    print("Debe ingresar solo letras")

            if dia == 1:
                if lunes1 == paciente:
                    lunes1 = ""
                    print("Turno cancelado con exito")
                elif lunes2 == paciente:
                    lunes2 = ""
                    print("Turno cancelado con exito")
                elif lunes3 == paciente:
                    lunes3 = ""
                    print("Turno cancelado con exito")
                elif lunes4 == paciente:
                    lunes4 = ""
                    print("Turno cancelado con exito")
                else:
                    print("El paciente no tiene turno asignado")
            else:
                if martes1 == paciente:
                    martes1 = ""
                    print("Turno cancelado con exito")
                elif martes2 == paciente:
                    martes2 = ""
                    print("Turno cancelado con exito")
                elif martes3 == paciente:
                    martes3 = ""
                    print("Turno cancelado con exito")
                else:
                    print("El paciente no tiene turno asignado")
        # OPCION 3
        elif opcion == 3:
            while True:
                print("1- LUNES")
                print("2- MARTES")
                dia = input("Selecione un dia:")

                if dia == "":
                    print("Debe ingresar una opcion para continuar")
                    print("")
                elif not dia.isdigit():
                    print("Ingrese un valor numerico")
                    print("")
                else:
                    dia = int(dia)

                    if dia < 1 or dia > 2:
                        print("Error opcion fuera de rango")
                    else:
                        break
            if dia == 1:
                print("Agenda dia lunes")
                if lunes1 == "":
                    print("Turno 1 libre")
                else:
                    print(f"Turno 1: {lunes1}")
                if lunes2 == "":
                    print("Turno 2 libre")
                else:
                    print(f"Turno 2: {lunes2}")
                if lunes3 == "":
                    print("Turno 3 libre")
                else:
                    print(f"Turno 3: {lunes3}")
                if lunes4 == "":
                    print("Turno 4 libre")
                else:
                    print(f"Turno 4: {lunes4}")
            else:
                print("Agenda dia martes")
                if martes1 == "":
                    print("Turno 1 libre")
                else:
                    print(f"Turno 1: {martes1}")
                if martes2 == "":
                    print("Turno 2 libre")
                else:
                    print(f"Turno 2: {martes2}")
                if martes3 == "":
                    print("Turno 3 libre")
                else:
                    print(f"Turno 3: {martes3}")

        # OPCION 4
        elif opcion == 4:
            ocupados_lunes = 0
            ocupados_martes = 0

            # Contador
            if lunes1 != "":
                ocupados_lunes = ocupados_lunes + 1

            if lunes2 != "":
                ocupados_lunes = ocupados_lunes + 1

            if lunes3 != "":
                ocupados_lunes = ocupados_lunes + 1

            if lunes4 != "":
                ocupados_lunes = ocupados_lunes + 1

            # Contador
            if martes1 != "":
                ocupados_martes = ocupados_martes + 1

            if martes2 != "":
                ocupados_martes = ocupados_martes + 1

            if martes3 != "":
                ocupados_martes = ocupados_martes + 1

            # Calculos de dias
            disponibles_lunes = 4 - ocupados_lunes
            disponibles_martes = 3 - ocupados_martes

            # Mostrar resumen
            print("----- RESUMEN GENERAL -----")
            print(f"Lunes: {ocupados_lunes} ocupados - {disponibles_lunes} disponibles")
            print(
                f"Martes: {ocupados_martes} ocupados - {disponibles_martes} disponibles"
            )

            # Moastrar resumen
            if ocupados_lunes > ocupados_martes:
                print("El lunes tiene más turnos ocupados")
            elif ocupados_martes > ocupados_lunes:
                print("El martes tiene más turnos ocupados")
            else:
                print("Hay empate en la cantidad de turnos ocupados")
        # OPCION 5
        elif opcion == 5:
            break
