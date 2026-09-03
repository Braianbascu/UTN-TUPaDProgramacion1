# Actividada Nº2

# Variables a usar

productos = []

for i in range(5):

    # Elegí usar solo letras para trabajar algunas validaciones
    while True:
        producto = input("Ingrese un producto: ")

        if producto == "":
            print("Debe ingresar un producto")
        elif not producto.isalpha():
            print("La carga solo admite letras")
        else:
            productos.append(producto)
            break

productos = sorted(productos)

print("")
print("--- LISTA DE PRODUCTOS ---")

for i in range(len(productos)):
    print(f"Producto: {i + 1}: {productos[i]}")

while True:
    opcion = input("¿Deseas eliminar algun producto? S/N: ")

    if opcion == "S" or opcion == "s":

        producto = input("Ingrese el producto a eliminar: ")

        if producto == "":
            print("Debe ingresar un producto")
        elif not producto.isalpha():
            print("La carga solo admite letras")
        elif producto in productos:
            productos.remove(producto)
            print("Producto eliminado correctamente")
            break
        else:
            print("El producto no se encuentra en la lista")

    elif opcion == "N" or opcion == "n":
        print("Programa terminado")
        break

    else:
        print("Debe ingresar una opcion correcta")

print("")
print("--- LISTA DE PRODUCTOS FINAL ---")

for i in range(len(productos)):
    print(f"Producto: {i + 1}: {productos[i]}")
