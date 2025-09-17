# Autor: Gio Antonio Canto Gomez
# Actividad: Suma de dos números
"""Descripción: Lee dos números reales y muestra su suma con validación de entrada."""

def leer_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Intente de nuevo con un número (ej. 3, 4.5).")

def main() -> None:
    a = leer_float("Ingresa el primer número: ")
    b = leer_float("Ingresa el segundo número: ")
    suma = a + b
    print(f"La suma de {a} + {b} = {suma}")

if __name__ == "__main__":
    main()
