# TRABAJO PRACTICO DE PROGRAMACION Nº1 - BASCUÑAN BRAIAN

# EJERCICIO Nº1

# Variables utilizadas
nombre_cliente = ""
cantidad_productos = 0
productos = []
valor_producto = 0
descuento = ""
valor_total = 0
valor_final = 0
valor_ahorro = 0
promedio_productos = 0

# Solicitud de nombre
while True:
    nombre_cliente = input("Ingrese nombre del cliente: ")
    if nombre_cliente == "":
        print("Debe ingresar un nombre para continuar")

    elif nombre_cliente.isalpha():
        break
    else:
        print("Debe ingresar solo letras")

# Solicitud cantidad final de productos
while True:
    cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")

    if cantidad_productos == "":
        print("Debe ingresar un valor")
    elif not cantidad_productos.isdigit():
        print("Debe ingresar un valor numerico")
    elif int(cantidad_productos) <= 0:
        print("Debe ingresar un valor mayor a 0")
    else:
        cantidad_productos = int(cantidad_productos)
        break

# Carga de valores
for i in range(cantidad_productos):

    while True:
        valor_producto = input(f"ingrese el valor entero del producto {i+1}: ")

        if valor_producto == "":
            print("Debe ingresar un valor")
        elif not valor_producto.isdigit():
            print("Debe ingresar un valor numerico")
        else:
            valor_producto = int(valor_producto)
            break

    while True:
        descuento = input("¿El producto posee descuento?: S/N: ")

        if descuento.lower() == "s":
            break
        elif descuento.lower() == "n":
            break
        else:
            print("Debe ingresar S o N")

    valor_total += valor_producto

    # Diferenciacion por descuento
    if descuento.lower() == "s":
        valor_ahorro += valor_producto * 0.10

    # Carga a la base de deatos
    productos.append(
        f"Producto {i + 1} - Precio: {valor_producto} Descuento (S/N): {descuento}"
    )

# Calculos
valor_final = valor_total - valor_ahorro
promedio_productos = valor_final / cantidad_productos

# Consola
print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")

for producto in productos:
    print(producto)

print(f"Total sin descuentos: ${valor_total}")
print(f"Total con descuentos: ${valor_final:.2f}")
print(f"Ahorro: ${valor_ahorro:.2f}")
print(f"Promedio por producto: ${promedio_productos:.2f}")
