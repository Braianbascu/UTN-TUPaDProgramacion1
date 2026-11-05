#       FUNCIONES DEL MENU
# -------------------------------


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
                        raise ValueError("Ya existe una herramienta con este nombre")

                break

            except ValueError as e:
                print(f"Error: {e}")

        # Validacion de stock
        while True:
            try:
                stock_herramienta = int(input("Ingrese el stock de la herramienta: "))

                if stock_herramienta < 0:
                    raise ValueError("El stock no puede ser menor a cero")

                break

            except ValueError as e:
                print(f"Error: {e}")

        # Carga herramiento al inventario
        inventario.append(
            {
                "herramienta": nombre_herramienta,
                "cantidad": stock_herramienta,
            }
        )
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
    # Auxiliar de busqueda
    busqueda = False

    # Verificacion inventario vacio
    if len(inventario) == 0:
        print("El inventario se encuentra vacio")
        return

    # Recepcion y validacion busqueda
    nombre_herramienta = input(
        "ingrese el nombre de la herramienta a consultar: "
    ).strip()
    print("")

    if nombre_herramienta == "":
        raise ValueError("El nombre no debe estar vacio")

    # Busqueda en inventario
    for herramienta in inventario:
        if nombre_herramienta.lower() == herramienta["herramienta"].lower():

            busqueda = True

            print(
                f"Se encontro la herramienta buscada: {herramienta['herramienta']} | stock: {herramienta['cantidad']}"
            )

    # Impresion en caso de no tener coincidencias
    if busqueda == False:
        print("No se encontro la herramienta en el inventario")

    print("")


# OPCION 4 - REPORTE DE AGOTADOS
def reporte_agotados(inventario):
    # Auxiliar de busqueda
    agotados = False

    # Verificacion inventario vacio
    if len(inventario) == 0:
        print("El inventario esta vacio")

    else:
        # Busqueda herramientas con stock 0
        for herramienta in inventario:
            if herramienta["cantidad"] == 0:

                agotados = True

                print(
                    f"Herramienta: {herramienta['herramienta']} | Stock: {herramienta['cantidad']}"
                )

        # Impresion en caso de no tener coincidencias
        if agotados == False:
            print("No existen herramientas con stock 0")

    print("")


# OPCION 5 - ALTA PRODUCTO
def alta_producto(inventario):

    # Validacion de nombre y stock
    nombre_herramienta = input("Ingrese el nombre de la herramienta: ").strip()

    if nombre_herramienta == "":
        raise ValueError("El nombre no puede estar vacio")

    # Busqueda de coincidencia
    for herramienta in inventario:
        if nombre_herramienta.lower() == herramienta["herramienta"].lower():
            raise ValueError("Ya existe una herramienta con este nombre")

    stock_herramienta = int(input("Ingrese el stock: "))

    # Control stock negativo
    if stock_herramienta < 0:
        raise ValueError("El producto no puede tener un stock negativo")

    # Carga herramiento al inventario
    inventario.append(
        {
            "herramienta": nombre_herramienta,
            "cantidad": stock_herramienta,
        }
    )

    print("")
    print("Herramienta cargada con exito")
    print("")


# OPCION 6 - ACTUALIZAR STOCK
def actualizar_stock(inventario):
    # Auxuliar de busqueda
    busqueda = False

    # Auxliar de diccionario
    herramienta_buscada = None

    # Verificacion inventario vacio
    if len(inventario) == 0:
        print("El inventario se encuentra vacio")
        return

    # Validacion de nombre y stock
    nombre_herramienta = input("Ingrese el nombre de la herramienta: ").strip()

    if nombre_herramienta == "":
        raise ValueError("El nombre no puede estar vacio")

    for herramienta in inventario:
        if nombre_herramienta.lower() == herramienta["herramienta"].lower():
            herramienta_buscada = herramienta
            busqueda = True
            print(
                f"Se encontro la herramienta buscada: {herramienta['herramienta']} | stock: {herramienta['cantidad']}"
            )
            print("")
            break

    if busqueda == False:
        print("No se encontro la herramienta en el inventario")
        print("")
        return

    print("--Menu de actualizacion--")
    print("")
    print("1 - Venta")
    print("2 - Ingreso")
    print("")

    opcion = input("Selecciones el numero de la operacion a realizar: ")
    print("")

    if opcion == "1":

        unidades_venta = int(input("Ingrese las unidades en venta: "))
        print("")

        if unidades_venta <= 0:
            raise ValueError("Las unidades deben ser mayores a cero")

        if unidades_venta > herramienta_buscada["cantidad"]:
            raise ValueError("No hay stock suficiente para realizar la operacion")

        herramienta_buscada["cantidad"] -= unidades_venta

        print("La venta se realizo con exito")
        print(f"Stock actual: {herramienta_buscada['cantidad']}")
        print("")

    elif opcion == "2":

        unidades_ingreso = int(input("Ingrese las unidades a ingresar: "))
        print("")

        if unidades_ingreso <= 0:
            raise ValueError("Las unidades deben ser mayores a cero")

        herramienta_buscada["cantidad"] += unidades_ingreso

        print("El ingreso se realizo con exito")
        print(f"Stock actual: {herramienta_buscada['cantidad']}")
        print("")

    else:
        print("Opcion ingresada invalida")
        return
