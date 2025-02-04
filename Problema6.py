# Solicitar al usuario la temperatura en grados Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir a grados Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Convertir a grados Kelvin
kelvin = celsius + 273.15

# Mostrar los resultados
print(f"{celsius}°C es equivalente a {fahrenheit:.2f}°F y {kelvin:.2f}K.")