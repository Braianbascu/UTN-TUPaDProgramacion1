# Actividad Nº8

# Variables a solicitar:

peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en metros: "))


# Definicion de funcion
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc


resultado = calcular_imc(peso, altura)

print(f"Su IMC es de: {resultado:.2f}")
