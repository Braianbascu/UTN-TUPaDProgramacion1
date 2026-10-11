# Actividad Nº10
# Menu de seleccion
while True:
    print("---SIMULADOR DE COMPUERTAS LOGICAS---")
    print("")
    print("1: Compuerta AND")
    print("2: Compuerta OR")
    print("3: Compuerta NOT")
    print("4: Salir")
    print("")

    opcion = input("Ingrese su eleccion: ")
    print("")
    # Validaciones opciones
    if opcion == "":
        print("Debe ingresar un valor")
        print("")
    elif not opcion.isdigit():
        print("Debe ingresar un valor numerico")
        print("")
    else:
        opcion = int(opcion)
        if opcion < 1 or opcion > 5:
            print("Error opcion fuera de rango")
            print("")
        else:
            break
