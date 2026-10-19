# Actividad Nº5

# Codigos con Try-Except, else y finally

# 1

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b

except TypeError:
    print("Ocurrio un error al ingresar un tipo de dato no valido para la operacion")

except Exception as e:
    print(f"Ocurrio un error al intentar realizar la division: {e}")

else:
    print("La operacion se realizo con exito")
    print(f"Resultado: {result}")

finally:
    print("Cerrando el programa...")

# 2

try:
    numbers = [
        1,
        2,
        3,
    ]
    print(numbers[5])

except IndexError:
    print("No se puede acceder al elemento ya que este no existe dentro de la lista")

except Exception as e:
    print(f"Ocurrio un error al intentar acceder: {e}")

else:
    print("El programa accedio con exito al elemento")

finally:
    print("Cerrando el programa...")
