# Actividad: Ahorcado (simple)
"""Descripción: Adivina la palabra con 6 intentos."""

import random

palabras = ["python", "codigo", "algoritmo", "programa"]
palabra = random.choice(palabras)
oculta = ["_"] * len(palabra)
usadas = set()
intentos = 6

print("Ahorcado. Tienes 6 intentos.")
while intentos > 0 and "_" in oculta:
    print("Palabra:", " ".join(oculta), "| Usadas:", ",".join(sorted(usadas)))
    letra = input("Letra: ").lower().strip()
    if len(letra) != 1 or not letra.isalpha() or letra in usadas:
        print("Entrada inválida o repetida.")
        continue
    usadas.add(letra)
    if letra in palabra:
        for i, ch in enumerate(palabra):
            if ch == letra:
                oculta[i] = letra
    else:
        intentos -= 1
        print(f"Fallaste. Intentos restantes: {intentos}")
        
print("¡Ganaste!" if "_" not in oculta else f"Perdiste. Era: {palabra}")
