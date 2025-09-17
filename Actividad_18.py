# Actividad: Lista de primos
"""Descripción: Muestra los primos menores a un límite dado."""

def es_primo(k: int) -> bool:
    if k <= 1:
        return False
    if k <= 3:
        return True
    if k % 2 == 0 or k % 3 == 0:
        return False
    i = 5
    while i * i <= k:
        if k % i == 0 or k % (i + 2) == 0:
            return False
        i += 6
    return True

lim = int(input("Límite (>2): "))
primos = [n for n in range(2, lim) if es_primo(n)]
print(primos if primos else f"No hay primos menores que {lim}")
