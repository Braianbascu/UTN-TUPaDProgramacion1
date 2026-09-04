# Actividada Nº9
# Solo use validaciones de rango, no implemente de esapcio vacio y letras para optimizar tiempo

# Variables a usar

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

print("--- TA-TE-TI ---")

# Controlador de juego
for turno in range(9):

    # Alternancia de turnos
    if turno % 2 == 0:
        simbolo = "X"
        jugador = 1
    else:
        simbolo = "O"
        jugador = 2

    # Pedir y validar posición
    while True:
        fila = int(input(f"Jugador {jugador} - Ingrese la fila (1-3): "))
        columna = int(input(f"Jugador {jugador} - Ingrese la columna (1-3): "))

        if fila < 1 or fila > 3 or columna < 1 or columna > 3:
            print("Posición fuera de rango. Intente nuevamente.")
        else:
            # Convertir posición 1-3 a índice 0-2
            fila -= 1
            columna -= 1

            if tablero[fila][columna] != "-":
                print("La casilla ya está ocupada. Elija otra.")
            else:
                break

    # Colocar ficha
    tablero[fila][columna] = simbolo

    # Mostrar tablero
    print()
    for fila_tablero in tablero:
        print(fila_tablero)

    # Verificar ganador
    ganador = False

    # Verificar filas
    for fila_tablero in tablero:
        if (
            fila_tablero[0] == simbolo
            and fila_tablero[1] == simbolo
            and fila_tablero[2] == simbolo
        ):
            ganador = True

    # Verificar columnas
    for columna_tablero in range(3):
        if (
            tablero[0][columna_tablero] == simbolo
            and tablero[1][columna_tablero] == simbolo
            and tablero[2][columna_tablero] == simbolo
        ):
            ganador = True

    # Verificar diagonal principal
    if (
        tablero[0][0] == simbolo
        and tablero[1][1] == simbolo
        and tablero[2][2] == simbolo
    ):
        ganador = True

    # Verificar diagonal secundaria
    if (
        tablero[0][2] == simbolo
        and tablero[1][1] == simbolo
        and tablero[2][0] == simbolo
    ):
        ganador = True

    # Ganador
    if ganador:
        print(f"¡Ganó el jugador {jugador} ({simbolo})!")
        break

else:
    print("¡Empate!")
