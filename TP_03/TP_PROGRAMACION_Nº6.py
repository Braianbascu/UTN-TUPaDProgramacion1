# Actividad º6

# Solicitud de numero

numero = int(input("Ingrese su numero a multiplicar: "))


# Definicion de funciones:
def tabla_multiplicar(numero):
    for i in range(1, 11):
        total = numero * i
        print(f"{numero} x {i} = {total}")


tabla_multiplicar(numero)
