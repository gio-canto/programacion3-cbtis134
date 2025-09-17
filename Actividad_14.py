# Actividad: Adivina el número
"""Descripción: Adivina un número secreto entre 1 y 100."""

import random

secreto = random.randint(1, 100)
intentos = 0
print("Adivina el número (1-100).")
while True:
    intento = int(input("Tu número: "))
    intentos += 1
    if intento == secreto:
        print(f"¡Acertaste! Intentos: {intentos}")
        break
    print("Es mayor." if intento < secreto else "Es menor.")
