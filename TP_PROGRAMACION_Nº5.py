# EJERCICIO Nº5

while True:
    nombre = input("ingrese el nombre del gladiador: ")

    if nombre == "":
        print("Error: Solo se permiten letras")
    elif nombre.isalpha():
        print("")
        break
    else:
        print("Error: Solo se permiten letras")

print(f"------BIENVENIDO {nombre}------")

# INICIO VARIABLES
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
daño_ataque_pesado = 15
daño_base_enemigo = 12
turno_gladiador = True

print("")
print("----------ARENA DE COMBATE----------")

# Inicio de ciclo
while vida_gladiador > 0 and vida_enemigo > 0:
    print("¡COMBATE!")
    print(f"vida {nombre}: {vida_gladiador}")
    print(f"vida enemigo: {vida_enemigo}")
    print(f"posiciones de vida: {pociones_vida}")
    print("")
    print("MENU")
    print("OPCION 1: ATAQUE PESADO ")
    print("OPCION 2: RAFAGA DE ATAQUE")
    print("OPCION 3: TOMAR POSCION DE CURA")

    opcion = input("Por favor ingrese una opcion: ")

    # Control
    while True:
        if opcion == "":
            print("Debe ingresar un valor")
        elif not opcion.isdigit():
            print("Debe ingresar un valor numerico")
        else:
            opcion = int(opcion)
            if opcion < 1 or opcion > 3:
                print("Error opcion fuera de rango")
            else:
                break
        opcion = input("Por favor ingrese una opcion: ")

    # Opciones

    if opcion == 1:
        if vida_enemigo < 20:
            daño = daño_ataque_pesado * 1.5
            print("Golpe Critico")
        else:
            daño = daño_ataque_pesado

        vida_enemigo -= daño
        print(f"Atacaste al enemigo por: {daño} puntos de vida")

    elif opcion == 2:
        for rafaga in range(3):
            input("Oprima Enter para atacar con rafaga!")
            vida_enemigo -= 5
            print("Golpe conectado por 5 de daño")
            print(f"Rafaga {rafaga+1}/3")
    elif opcion == 3:
        if pociones_vida > 0:
            vida_gladiador += 30
            pociones_vida -= 1
            print("30 puntos de vida restaurados")

            if vida_gladiador > 100:
                vida_gladiador = 100

        else:
            print("No te quedan posciones")

    turno_gladiador = False
    print("Turno del rival")
    print("")

    vida_gladiador -= daño_base_enemigo
    print("El enemigo ataco, pierdes 15 puntos de vida")
    print("")
    turno_gladiador = True
    print("Es tu tunrno")


if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} GANO LA BATALLA!.")
else:
    print("¡DERROTA, EL ENEMIFO VENCIO!")
