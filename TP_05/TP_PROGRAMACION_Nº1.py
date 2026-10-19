# Actividad Nº1

# Codigos a analizar

# 1
a = 10
b = input(
    "Introduce un número: "
)  # No hay conversion de datos, sera tomado como string. input () devolvera un stirng
result = a / b  # no se puede realizar la operacion por los tipos de datos, TypeError
print(f"Resultado: {result}")

# 2
numbers = [1, 2, 3]
print(numbers[5])  # Ingreso a un indice inexistente, IndexError
