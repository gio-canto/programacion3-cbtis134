# Actividad: Número mayor
"""Descripción: Lee dos números y muestra el mayor o si son iguales."""

x = float(input("Ingresa el primer número: "))
y = float(input("Ingresa el segundo número: "))
if x > y:
    print(f"El número mayor es: {x}")
elif y > x:
    print(f"El número mayor es: {y}")
else:
    print("Son iguales")
