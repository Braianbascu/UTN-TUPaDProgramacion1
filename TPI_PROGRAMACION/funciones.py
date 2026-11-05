# FUNCIONES AUXILIARES


# VALIDAR OPCIONES
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


# FUNCIONES DEL MENU


# OPCION 1 - CARGAR HERRAMIENTAS
def cargar_herramientas(inventario):

    # Solcitud de cantidad de herramientas
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos a cargar: "))
            print("")

            if cantidad <= 0:
                raise ValueError("Debe ingresar un numero mayor a cero")
            break

        except ValueError as e:
            print(f"Error: {e}")

    # Carga de herramientas
    for i in range(cantidad):
        print(f"Cargando herramienta {i + 1}")

        # Validacion de nombre
        while True:
            try:
                nombre_herramienta = input(
                    "Ingrese el nombre de la herramienta: "
                ).strip()

                if nombre_herramienta == "":
                    raise ValueError("El nombre no puede estar vacio")

                for herramienta in inventario:
                    if nombre_herramienta.lower() == herramienta["herramienta"].lower():
                        raise ValueError(
                            "Error, ya existe una herramienta con este nombre"
                        )

                break

            except ValueError as e:
                print(f"Error: {e}")

        # Validacion de stock
        while True:
            try:
                stock_herramienta = int(input("Ingrese el stock de la herramienta: "))

                if stock_herramienta < 0:
                    raise ValueError("Error, el stock no puede ser menor a cero")

                break

            except ValueError as e:
                print(f"Error: {e}")

        herramienta = {
            "herramienta": nombre_herramienta,
            "cantidad": stock_herramienta,
        }

        inventario.append(herramienta)
        print("")
        print("Herramienta cargada con exito")
        print("")


# OPCION 2 - CARGAR INVENTARIO HERRAMIENTAS
def mostrar_inventario(inventario):

    # Verificar si existen prductos
    if len(inventario) == 0:
        print("El inventario esta vacio")

    # Impresion de Inventario
    else:
        print("--INVENTARIO DE HERRAMIENTAS--")
        for herramienta in inventario:
            print(
                f"Herramienta: {herramienta['herramienta']} | Stock: {herramienta['cantidad']}"
            )

    print("")


# OPCION 3 - CONSULTAR STOCK
def consultar_stock(inventario):

    busqueda = False

    if len(inventario) == 0:
        print("El inventario se encuentra vacio")
        return

    nombre_herramienta = input(
        "ingrese el nombre de la herramienta a consultar: "
    ).strip()
    print("")

    if nombre_herramienta == "":
        raise ValueError("El nombre no debe estar vacio")

    for herramienta in inventario:
        if nombre_herramienta.lower() == herramienta["herramienta"].lower():

            busqueda = True

            print(
                f"Se encontro la herramienta buscada: {herramienta['herramienta']} | stock: {herramienta['cantidad']}"
            )

    if busqueda == False:
        print("No se encontro la herramienta en el inventario")

    print("")


# OPCION 4 - REPORTE DE AGOTADOS
def reporte_agotados(inventario):

    agotados = False

    if len(inventario) == 0:
        print("El inventario esta vacio")
    else:

        for herramienta in inventario:
            if herramienta["cantidad"] == 0:

                agotados = True

                print(
                    f"Herramienta: {herramienta['herramienta']} | Stock: {herramienta['cantidad']}"
                )

        if agotados == False:
            print("No existen herramientas con stock 0")

    print("")


# OPCION 5 - ALTA PRODUCTO
def alta_producto(inventario):

    # Validacion de nombre y stock
    nombre_herramienta = input("Ingrese el nombre de la herramienta: ").strip()

    if nombre_herramienta == "":
        raise ValueError("El nombre no puede estar vacio")

    for herramienta in inventario:
        if nombre_herramienta.lower() == herramienta["herramienta"].lower():
            raise ValueError("Error, ya existe una herramienta con este nombre")

    stock_herramienta = int(input("Ingrese el stock: "))

    if stock_herramienta < 0:
        raise ValueError("El producto no puede tener un stock negativo")

    herramienta = {
        "herramienta": nombre_herramienta,
        "cantidad": stock_herramienta,
    }

    inventario.append(herramienta)
    print("")
    print("Herramienta cargada con exito")
    print("")
