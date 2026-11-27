# ACTIVIDAD Nº9
# GESTOR DE PRODUCTOS

# FUNCIONES


# 1 - MOSTRAR PRODUCTOS
def mostrar_productos(productos):

    for producto in productos:

        print(
            f"Producto: {producto['nombre']} | "
            f"Precio: ${producto['precio']} | "
            f"Cantidad: {producto['cantidad']}"
        )


# 2 - AGREGAR PRODUCTOS
def agregar_productos(productos):

    nombre = input("Ingrese el nombre del producto: ").strip()
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}

    productos.append(producto)

    print("Producto agregado correctamente")


# 3 - CARGAR PRODUCTOS EN UNA LISTA
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


# 4 - BUSCAR PRODUCTOS
def buscar_producto(productos):

    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()

    for producto in productos:

        if producto["nombre"].lower() == nombre_buscado.lower():

            print(f"Producto: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            return

    print("Producto no encontrado")


# 5 - GUARDAR PRODUCTOS AGREGADOS EN TXT
def guardar_productos(productos):

    with open("productos.txt", "w", encoding="utf-8") as archivo:

        for producto in productos:

            archivo.write(
                f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            )

    print("Productos guardados correctamente")


# PROGRAMA PRINCIPAL


def mostrar_menu():

    print("")
    print("--- SISTEMA DE GESTION DE PRODUCTOS ---")
    print("")
    print("1- Mostrar productos")
    print("2- Agregar productos")
    print("3- Buscar productos")
    print("4- Guardar productos en la base de datos")
    print("5- Salir")
    print("")


def main():

    productos = cargar_productos()

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
            mostrar_productos(productos)

        elif opcion == 2:
            agregar_productos(productos)

        elif opcion == 3:
            buscar_producto(productos)

        elif opcion == 4:
            guardar_productos(productos)

        elif opcion == 5:
            print("Finalizando el programa...")


main()
