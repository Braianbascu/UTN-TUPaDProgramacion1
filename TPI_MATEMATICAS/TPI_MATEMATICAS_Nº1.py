# SIMULADOR DE COMPUERTAS LOGICAS

# MENU POR CONSOLA DE OPCIONES
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

    # VALIDACION DE INPUT
    if opcion == "":
        print("Debe ingresar un valor")
        print("")
    elif not opcion.isdigit():
        print("Debe ingresar un valor numerico")
        print("")
    else:
        opcion = int(opcion)
        if opcion < 1 or opcion > 4:
            print("Error opcion fuera de rango")
            print("")
        else:

            # COMPUERTA AND
            if opcion == 1:
                print("Seleccionaste la compuerta AND")

                # VALIDACIONES DE ENTRADAS
                a = input("Ingresa el primer valor (0 o 1): ")

                while a != "0" and a != "1":
                    print("Error: solo se permite ingresar 0 o 1")
                    a = input("Ingresa el primer valor (0 o 1): ")

                b = input("Ingresa el segundo valor (0 o 1): ")

                while b != "0" and b != "1":
                    print("Error: solo se permite ingresar 0 o 1")
                    b = input("Ingresa el segundo valor (0 o 1): ")

                # IMPRESION DE RESULTADOS POR CONSOLA Y BREVE EXPLICACION
                if a == "1" and b == "1":
                    print("")
                    resultado = "1"
                    print(
                        "Este resultado, es producto a que ambos valores de entrada son 1"
                    )
                else:
                    print("")
                    resultado = "0"
                    print(
                        "Este resultado, es producto a que al menos un valor de entrada es 0"
                    )

                print("Resultado de AND:", resultado)
                print("")

            # COMPUERTA OR
            elif opcion == 2:
                print("Seleccionaste la compuerta OR")

                # VALIDACIONES DE ENTRADAS
                a = input("Ingresa el primer valor (0 o 1): ")

                while a != "0" and a != "1":
                    print("Error: solo se permite ingresar 0 o 1")
                    a = input("Ingresa el primer valor (0 o 1): ")

                b = input("Ingresa el segundo valor (0 o 1): ")

                while b != "0" and b != "1":
                    print("Error: solo se permite ingresar 0 o 1")
                    b = input("Ingresa el segundo valor (0 o 1): ")

                # IMPRESION DE RESULTADOS POR CONSOLA Y BREVE EXPLICACION
                if a == "1" or b == "1":
                    print("")
                    resultado = "1"
                    print("Este resultado, es producto a que al menos una entrada es 1")
                else:
                    print("")
                    resultado = "0"
                    print("Este resultado, es producto a que ambas entradas son 0")

                print("Resultado de OR:", resultado)
                print("")
