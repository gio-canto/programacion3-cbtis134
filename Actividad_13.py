# Actividad: Factorial
"""Descripción: Calcula el factorial de un entero n >= 0."""

n = int(input("Ingresa un entero no negativo: "))
if n < 0:
    print("Debe ser no negativo.")
else:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(f"{n}! = {fact}")
