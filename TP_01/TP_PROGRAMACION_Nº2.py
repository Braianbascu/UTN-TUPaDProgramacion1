# EJERCICIO Nº2

# Variables utilizadas

usuario_correcto = "alumno"
contraseña_correcta = "python123"
acceso = False

for intento in range(1, 4):
    print(f"intento: {intento}")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario_correcto == usuario and contraseña_correcta == contraseña:
        print("Acceso concedido")
        print("")
        acceso = True
        break
    else:
        print("Credenciales invalidas")

if acceso == False:
    print("Cuenta bloqueada")
else:
    while True:
        print("-----MENU-----")
        print("")
        print("1- Estado de inscripcion")
        print("2- Cambiar contraseña")
        print("3- Mostrar mensaje motivacional")
        print("4- Salir")
        print("")

        opcion = input("Elegi una opcion: ")

        if not opcion.isdigit():
            print("Ingrese un valor numerico")
        else:
            opcion = int(opcion)

            if opcion < 1 or opcion > 4:
                print("Error opcion fuera de rango")
            else:
                if opcion == 1:
                    print("INSCRIPTO")
                elif opcion == 2:
                    nueva_contraseña = input("Ingrese su nueva contraseña: ")

                    if len(nueva_contraseña) < 6:
                        print("La contraseña debe tener minimo 6 caracteres")
                    else:
                        confirmacion = input("confirme su contraseña nueva: ")
                        if nueva_contraseña == confirmacion:
                            print("Contraseña cambiada con exito")
                            contraseña_correcta = nueva_contraseña
                        else:
                            print("Las contraseñas no coinciden")
                elif opcion == 3:
                    print("Cada pequeño paso que das te acerca a tus objetivos")
                elif opcion == 4:
                    break

                print("")
