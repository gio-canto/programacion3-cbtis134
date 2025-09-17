# Actividad: Piedra, papel o tijera
"""Descripción: Juega una ronda contra la computadora."""

import random

opciones = ["piedra", "papel", "tijera"]
jugador = input("Elige (piedra, papel, tijera): ").strip().lower()
if jugador not in opciones:
    print("Opción inválida.")
else:
    maquina = random.choice(opciones)
    print(f"La máquina eligió: {maquina}")
    if jugador == maquina:
        print("Empate")
    elif (jugador == "piedra" and maquina == "tijera") or          (jugador == "papel" and maquina == "piedra") or          (jugador == "tijera" and maquina == "papel"):
        print("Ganaste")
    else:
        print("Perdiste")
