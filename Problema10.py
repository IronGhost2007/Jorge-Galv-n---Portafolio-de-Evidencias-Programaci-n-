def calcular_area_triangulo():
    try:
        # Solicitar la base y la altura del triángulo
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        
        # Calcular el área
        area = (base * altura) / 2
        
        # Mostrar el resultado
        print(f"El área del triángulo es: {area}")
        
    except ValueError:
        print("Error: Ingrese solo valores numéricos.")

# Ejecutar la función
calcular_area_triangulo()
