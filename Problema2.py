# Solicitar al usuario dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Comparar los números
if numero1 > numero2:
    print(f"El primer número ({numero1}) es mayor que el segundo número ({numero2}).")
elif numero1 < numero2:
    print(f"El segundo número ({numero2}) es mayor que el primer número ({numero1}).")
else:
    print(f"Ambos números son iguales ({numero1}).")