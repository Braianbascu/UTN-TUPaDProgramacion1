# Actividad Nº6

try:
    numero = int(input("Ingrese un numero entero: "))

except ValueError:
    print("Debe ingresar un numero valido")

except Exception as e:
    print(f"Ocurrio un error al ingresar el valor: {e}")

else:
    print(f"Su numero ingresado es: {numero}")

finally:
    print("Cerrando el programa...")
