# Actividad: Conversor de temperatura
"""Descripción: Convierte entre Celsius y Fahrenheit según la opción elegida."""

op = input("Convierte desde (C)elsius o (F)ahrenheit: ").strip().upper()
if op == "C":
    c = float(input("Ingresa °C: "))
    f = (c * 9/5) + 32
    print(f"{c} °C = {f} °F")
elif op == "F":
    f = float(input("Ingresa °F: "))
    c = (f - 32) * 5/9
    print(f"{f} °F = {c} °C")
else:
    print("Opción no válida")
