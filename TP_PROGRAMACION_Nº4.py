# EJERCICIO Nº4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador_forzadas = 0


while True:
    agente = input("ingrese el nombre del agente: ")

    if agente == "":
        print("Debe ingresar un nombre para continuar")
    elif agente.isalpha():
        print("")
        break
    else:
        print("El nombre debe contener solo letras")

print(f"Bienvenido {agente}")


# menu de seleccion
while True:

    print("-----ESTADO-----")
    print(f"energia: {energia}")
    print(f"tiempo: {tiempo}")
    print(f"cerraduras abiertas: {cerraduras_abiertas}")
    print(f"alarma: {alarma}")
    print("")
    print("")
    print("-----MENU-----")
    print("")
    print("1- FORZAR CERRADURA")
    print("2- HACKEAR PANEL")
    print("3- DESCANSAR")
    print("")

    opcion = input("Seleccione una opcion: ")
    print("")

    # Control input ingresado

    if opcion == "":
        print("Debe ingresar una opcion para continuar")
        print("")
    elif not opcion.isdigit():
        print("Ingrese un valor numerico")
        print("")
    else:
        opcion = int(opcion)
        if opcion < 1 or opcion > 3:
            print("Error opcion fuera de rango")

        # Flujo de menu

        # FORZAR CERRADURA
        elif opcion == 1:
            energia -= 20
            tiempo -= 2
            contador_forzadas += 1

            if contador_forzadas == 3:
                alarma = True
                print("Cerradura sin abrir")
            else:
                if energia < 40:

                    numero = input("Ingrese un numero del 1 al 3: ")

                    while (
                        numero == ""
                        or not numero.isdigit()
                        or int(numero) < 1
                        or int(numero) > 3
                    ):
                        print("Ingrese un número válido del 1 al 3")
                        numero = input("Ingrese un numero del 1 al 3: ")

                    numero = int(numero)

                    if numero == 3:
                        alarma = True
                        print("¡Alarma activada!")
                        print("")
                    else:
                        cerraduras_abiertas += 1
                else:
                    cerraduras_abiertas += 1

        # HACKEAR PANEL
        elif opcion == 2:
            energia -= 10
            tiempo -= 3
            contador_forzadas = 0

            for paso in range(4):
                input("Oprima ENTER para hackear el panel...")
                codigo_parcial += "A"
                print(f"Paso {paso + 1}/4 completado")

            if len(codigo_parcial) >= 8:
                print("Panel hackeado por completo")
                cerraduras_abiertas += 1
                codigo_parcial = ""
            else:
                print(f"Progreso del código: {len(codigo_parcial)}/8")
        elif opcion == 3:
            contador_forzadas = 0
            energia += 15
            tiempo -= 1

            if energia > 100:
                energia = 100

            if alarma == True:
                energia -= 10

    # RESULTADOS DEL JUEGIO
    if cerraduras_abiertas == 3:
        print("VICTORIA: Bóveda abierta.")
        break

    if energia <= 0 or tiempo <= 0:
        print("DERROTA: Te quedaste sin energía o tiempo.")
        break

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("DERROTA: Alarma activa y poco tiempo")
        break
