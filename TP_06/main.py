# ACTIVIDAD Nº9
# GESTOR DE PRODUCTOS

# FUNCIONES


# 1 - MOSTRAR PRODUCTOS
def mostrar_productos():

    with open("productos.txt", "r", encoding="utf-8") as archivo:

        for linea in archivo:
            datos = linea.strip().split(",")

            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]

            print(f"Producto:{nombre} | Precio:{precio} | Cantidad:{cantidad}")


# 2 - CARGAR PRODUCTOS EN UNA LISTA
def cargar_productos():

    productos = []

    with open("productos.txt", "r", encoding="utf-8") as archivo:

        for linea in archivo:
            datos = linea.strip().split(",")

            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2]),
            }

            productos.append(producto)

    return productos


# PROGRAMA PRINCIPAL


# Impresion de menu
def mostrar_menu():
    print("")
    print("---SISTEMA DE GESTION DE PRODUCTOS---")
    print("")
    print("1- Mostrar productos")
    print("2- Agregar productos")
    print("3- Buscar productos")
    print("4- Guardar productos")
    print("5- Salir")
    print("")


# Menu y validacion de opciones
def main():

    opcion = 0

    while opcion != 5:
        mostrar_menu()

        while True:
            seleccion = input("Ingrese una opcion: ").strip()
            print("")

            if seleccion == "":
                print("Debe ingresar un valor")
                print("")

            elif not seleccion.isdigit():
                print("Debe ingresar un valor numerico")
                print("")

            elif int(seleccion) < 1 or int(seleccion) > 5:
                print("Opcion fuera de rango")
                print("")

            else:
                opcion = int(seleccion)
                break

        if opcion == 1:
            mostrar_productos()

        elif opcion == 2:
            cargar_productos()

        elif opcion == 3:
            print("Buscar productos")

        elif opcion == 4:
            print("Guardar productos")

        elif opcion == 5:
            print("Finalizando el programa...")


main()
