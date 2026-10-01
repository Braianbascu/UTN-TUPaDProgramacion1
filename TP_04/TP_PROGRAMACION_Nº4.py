# Actividada Nº4

# Variables a usar
contactos = {}

# Ingreso de datos
for i in range(5):
    nombre = input("Por favor ingrese un nombre de contacto: ")
    telefono = input("Por favor ingrese un numero telefonico: ")

    contactos[nombre] = telefono

# Variable de busqueda
buscar = input("Ingrese el nombre del contacto a buscar: ")

# Busqueda condicional
if buscar in contactos:
    print(f"el numero de {buscar} es: {contactos[buscar]}")
else:
    print("El contacto no existe")
