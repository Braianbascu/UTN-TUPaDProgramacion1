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

    opcion = input("Ingrese su eleccion: ").strip()
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
                a = input("Ingresa el primer valor (0 o 1): ").strip()

                while a != "0" and a != "1":
                    print("Error: solo se permite ingresar 0 o 1")
                    a = input("Ingresa el primer valor (0 o 1): ").strip()

                b = input("Ingresa el segundo valor (0 o 1): ").strip()

                while b != "0" and b != "1":
                    print("Error: solo se permite ingresar 0 o 1")
                    b = input("Ingresa el segundo valor (0 o 1): ").strip()

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
                a = input("Ingresa el primer valor (0 o 1): ").strip()

                while a != "0" and a != "1":
                    print("Error: solo se permite ingresar 0 o 1")
                    a = input("Ingresa el primer valor (0 o 1): ").strip()

                b = input("Ingresa el segundo valor (0 o 1): ").strip()

                while b != "0" and b != "1":
                    print("Error: solo se permite ingresar 0 o 1")
                    b = input("Ingresa el segundo valor (0 o 1): ").strip()

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

            # COMPUERTA NOT
            elif opcion == 3:
                print("Seleccionaste la compuerta NOT")

                # VALIDACION DE ENTRADA
                a = input("Ingrese un valor (0 o 1): ").strip()

                while a != "0" and a != "1":
                    print("Error: Solo se permite ingresar 0 o 1")
                    a = input("Ingrese un valor (0 o 1): ").strip()

                # IMPRESION DE RESULTADOS POR CONSOLA Y BREVE EXPLICACION
                if a == "0":
                    print("")
                    resultado = "1"
                    print("El resultado es 1 ya que la entrada fue invertida por NOT")
                else:
                    print("")
                    resultado = "0"
                    print("El resultado es 0 ya que la entrada fue invertida por NOT")

                print("Resultado de NOT:", resultado)
                print("")

            # SALIDA DEL PROGRAMA
            elif opcion == 4:
                print("Saliendo del programa...")
                break
