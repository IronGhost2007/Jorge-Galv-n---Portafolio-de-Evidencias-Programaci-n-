def operaciones_basicas():
    try:
        # Solicitar entrada de dos números enteros
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        
        # Realizar operaciones
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        
        # Manejo de división por cero
        if num2 != 0:
            division = num1 / num2
            division_piso = num1 // num2
            residuo = num1 % num2
        else:
            division = "Indefinida (división por cero)"
            division_piso = "Indefinida (división por cero)"
            residuo = "Indefinido (división por cero)"
        
        # Mostrar resultados
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")
        print(f"División de piso: {division_piso}")
        print(f"Residuo: {residuo}")
        
    except ValueError:
        print("Error: Ingrese solo números enteros.")

# Ejecutar la función
operaciones_basicas()
