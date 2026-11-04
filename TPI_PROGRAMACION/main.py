# Trabajo Integrador Programacion 1


# Funciones
def cargar_herramientas(inventario):
    print("1")


def mostrar_inventario(inventario):
    print("2")


def consultar_stock(inventario):
    print("3")


def reporte_agotados(inventario):
    print("4")


def alta_producto(inventario):
    print("5")


def actualizar_stock(inventario):
    print("6")


def validar_opcion(minimo, maximo):
    while True:

        opcion = input("Ingrese su eleccion: ")
        print("")

        # Validaciones opcione
        if opcion == "":
            print("Debe ingresar un valor")
            print("")

        elif not opcion.isdigit():
            print("Debe ingresar un valor numerico")
            print("")

        else:
            opcion = int(opcion)
            if opcion < minimo or opcion > maximo:
                print("Error opcion fuera de rango")
                print("")
            else:
                return opcion


# Menu principal


def main():
    inventario = []

    while True:
        # INTERFACE DE USUARIO
        print("-----------------------------")
        print("SISTEMA DE GESTION FERRETERIA")
        print("-----------------------------")
        print("")
        print("-------------MENU------------")
        print("")
        print("1 - CARGAR HERRAMIENTAS")
        print("2 - MOSTRAR INVENTARIO")
        print("3 - CONSULTAR STOCK")
        print("4 - REPORTE DE AGOTADOS")
        print("5 - ALTA DE PRODUCTO")
        print("6 - ACTUALIZAR STOCK")
        print("7 - SALIR")
        print("")

        # INGRESO OPCION
        opcion = validar_opcion(1, 7)

        # FUNCIONES DEL MENU

        if opcion == 1:
            cargar_herramientas(inventario)
            print("Opcion 1")

        elif opcion == 2:
            print("Opcion 2")
            mostrar_inventario(inventario)

        elif opcion == 3:
            consultar_stock(inventario)
            print("Opcion 3")

        elif opcion == 4:
            reporte_agotados(inventario)
            print("Opcion 4")

        elif opcion == 5:
            alta_producto(inventario)
            print("Opcion 5")

        elif opcion == 6:
            actualizar_stock(inventario)
            print("Opcion 6")

        elif opcion == 7:
            print("Saliendo del sistema...")
            break


main()
