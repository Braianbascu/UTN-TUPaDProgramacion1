# TRABAJO PRACTICO INTEGRADOR PROGRAMACION Nº1

# IMPORTACIONES
from funciones import cargar_herramientas
from funciones import validar_opcion
from funciones import mostrar_inventario
from funciones import reporte_agotados
from funciones import alta_producto
from funciones import consultar_stock


def actualizar_stock(inventario):
    print("6")


# Menu principal


# funcion de ejecucion
def main():
    inventario = []

    while True:
        try:
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

            elif opcion == 2:
                mostrar_inventario(inventario)

            elif opcion == 3:
                consultar_stock(inventario)

            elif opcion == 4:
                reporte_agotados(inventario)

            elif opcion == 5:
                alta_producto(inventario)

            elif opcion == 6:
                actualizar_stock(inventario)

            elif opcion == 7:
                print("Saliendo del sistema...")
                break

        except ValueError as e:
            print(f"Error: {e}")


main()
