# Solicitar al usuario su peso y altura
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el resultado
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

# Clasificación del IMC
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Clasificación: Peso normal")
elif 25 <= imc < 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")