# Actividad Nº8

# Variables a usar

productos = {
    "Pan": 2,
    "Yerba": 3,
    "Azucar": 4,
    "Banana": 7,
    "Papas": 3,
    "Coca Cola": 8,
    "Leche": 5,
    "Jabon": 7,
}

# Interface de usuario
print("---Sistema de mercado---")
print("------------------------")

while True:
    print("Menu de seleccion")
    print("")
    print("1 - Consultar stock de un producto")
    print("2 - Agregar stock")
    print("3 - Cargar nuevo producto")
    print("4 - Salir ")

    opcion = input("Ingrese la opcion deseada: ")
    # Menu interactivo
    if opcion == "":
        print("Debe ingresar un valor")

    elif not opcion.isdigit():
        print("Debe ingresar un valor numerico")

    else:
        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error opcion fuera de rango")

        elif opcion == 1:
            producto = input("Ingrese el producto a consultar: ")

            if producto in productos:
                print(f"El producto tiene un stock de: {productos[producto]}")
            else:
                print("El producto ingresado no existe")

        elif opcion == 2:
            producto = input("Ingrese su producto a agregar stock: ")

            if producto in productos:
                stock = int(input("Ingrese la cantidad de stock a agregar: "))
                productos[producto] += stock
            else:
                print("El producto no existe")

        elif opcion == 3:
            producto = input("Ingrese el nombre del nuevo producto: ")

            if producto in productos:
                print("El producto ingresado ya existe")
            else:
                stock = int(input("Ingrese el stock del producto nuevo: "))
                productos[producto] = stock
                print("Producto agregado correctamente")

        elif opcion == 4:
            print("Saliendo del sistema...")
            break
