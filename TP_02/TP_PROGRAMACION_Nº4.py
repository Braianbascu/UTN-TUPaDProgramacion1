# Actividad Nº4

# Lista original repetida
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_filtrados = []

# Lista filtrada con metodo
# datos = set(datos)


# Lista filtrada con bucle
for dato in datos:
    if dato not in datos_filtrados:
        datos_filtrados.append(dato)


# Mostrar resultado con iteracion (pedido de la consiga inicial)
print("Lista filtrada")
for i in datos_filtrados:
    print(f"numero: {i}")
