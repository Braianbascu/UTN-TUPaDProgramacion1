# TPI Nº2 MATEMATICAS

# Funcion para solicitar numeros enteros positivos o cero


def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < 0:
                print("Error: debe ingresar un numero positivo o cero.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un numero entero.")


# Solicitud de datos del universo
universo = input("Ingrese el nombre del universo: ")
total_universo = pedir_entero("Ingrese la cantidad total de jugadores: ")

# Solicitud de datos de los conjuntos
conjunto_A = input("Ingrese el nombre del conjunto A: ")
cantidad_A = pedir_entero("Ingrese la cantidad de jugadores del conjunto A: ")

conjunto_B = input("Ingrese el nombre del conjunto B: ")
cantidad_B = pedir_entero("Ingrese la cantidad de jugadores del conjunto B: ")

conjunto_C = input("Ingrese el nombre del conjunto C: ")
cantidad_C = pedir_entero("Ingrese la cantidad de jugadores del conjunto C: ")


# Solicitud de datos de las intersecciones
inter_AB = pedir_entero(
    "Ingrese la cantidad de jugadores que asisten lunes y miercoles: "
)
inter_AC = pedir_entero(
    "Ingrese la cantidad de jugadores que asisten lunes y viernes: "
)
inter_BC = pedir_entero(
    "Ingrese la cantidad de jugadores que asisten miercoles y viernes: "
)

inter_ABC = pedir_entero("Ingrese la cantidad de jugadores que asisten los tres dias: ")


# Validacion de los datos ingresados
if total_universo == 0:
    print("Error: el universo debe tener al menos un jugador.")

elif (
    cantidad_A > total_universo
    or cantidad_B > total_universo
    or cantidad_C > total_universo
):
    print("Error: un conjunto no puede superar la cantidad total del universo.")

elif inter_AB > cantidad_A or inter_AB > cantidad_B:
    print("Error: la interseccion AB supera la cantidad de uno de sus conjuntos.")

elif inter_AC > cantidad_A or inter_AC > cantidad_C:
    print("Error: la interseccion AC supera la cantidad de uno de sus conjuntos.")

elif inter_BC > cantidad_B or inter_BC > cantidad_C:
    print("Error: la interseccion BC supera la cantidad de uno de sus conjuntos.")

elif inter_ABC > inter_AB or inter_ABC > inter_AC or inter_ABC > inter_BC:
    print(
        "Error: la interseccion de los tres conjuntos no puede superar las intersecciones de dos conjuntos."
    )

else:

    # Calculo de las intersecciones exclusivas
    solo_AB = inter_AB - inter_ABC
    solo_AC = inter_AC - inter_ABC
    solo_BC = inter_BC - inter_ABC

    # Calculo de jugadores que asisten solamente un dia
    solo_A = cantidad_A - solo_AB - solo_AC - inter_ABC
    solo_B = cantidad_B - solo_AB - solo_BC - inter_ABC
    solo_C = cantidad_C - solo_AC - solo_BC - inter_ABC

    # Verificacion de las regiones exclusivas
    if solo_A < 0 or solo_B < 0 or solo_C < 0:
        print(
            "Error: los datos de las intersecciones no son coherentes con las cantidades de los conjuntos."
        )

    else:

        # Calculo de jugadores que asisten al menos un dia
        total_asistentes = (
            solo_A + solo_B + solo_C + solo_AB + solo_AC + solo_BC + inter_ABC
        )

        # Calculo de jugadores que no asisten ningun dia
        ninguno = total_universo - total_asistentes

        # Validacion del total del universo
        if ninguno < 0:
            print(
                "Error: la cantidad de jugadores que asisten supera el total del universo."
            )

        else:

            # Presentacion de resultados
            print("\n--- RESULTADOS DEL TRABAJO ---")

            print("Universo:", universo)
            print("Total de jugadores:", total_universo)

            print("\nIntersecciones exclusivas:")
            print("Solamente", conjunto_A, "y", conjunto_B, ":", solo_AB)
            print("Solamente", conjunto_A, "y", conjunto_C, ":", solo_AC)
            print("Solamente", conjunto_B, "y", conjunto_C, ":", solo_BC)

            print("\nJugadores que asisten solamente un dia:")
            print(conjunto_A, ":", solo_A)
            print(conjunto_B, ":", solo_B)
            print(conjunto_C, ":", solo_C)

            print("\nJugadores que asisten los tres dias:", inter_ABC)

            print("\nJugadores que asisten al menos un dia:", total_asistentes)
            print("Jugadores que no asisten ningun dia:", ninguno)
