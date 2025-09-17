# Actividad: ¿Es primo?
"""Descripción: Verifica si un número entero es primo."""

n = int(input("Ingresa un entero: "))

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

print(f"{n} es primo" if es_primo(n) else f"{n} no es primo")
