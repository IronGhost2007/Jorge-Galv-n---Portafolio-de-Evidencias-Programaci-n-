# Solicitar al usuario el precio del producto y el porcentaje de descuento
precio = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

# Calcular el monto del descuento
monto_descuento = (descuento / 100) * precio

# Calcular el precio final después del descuento
precio_final = precio - monto_descuento

# Mostrar el precio final
print(f"El precio final después de un {descuento}% de descuento es: {precio_final:.2f}")