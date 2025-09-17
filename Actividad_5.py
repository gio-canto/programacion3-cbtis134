
# Autor: Gio Antonio Canto Gomez
# Actividad: Bucles en Python (for / while)
"""Descripción: Esto presenta un menú de ejercicios con bucles (PARA / MIENTRAS):
Contar 1..10, Factorial de N, Imprimir palabras y conteo, Serie Fibonacci,
Triángulo de asteriscos, Suma hasta -1, PIN con 3 intentos, Hipotenusa validada,
Calculadora en bucle y Combate por turnos."""

import math
import random
import time

def contar_1_a_10():
    print("\n--- Contar del 1 al 10 ---")
    for i in range(1, 11):
        print(i)

def factorial_n():
    print("\n--- Factorial de N ---")
    n = int(input("Dame el valor del factorial a calcular (entero ≥ 0): "))
    base = 1
    for i in range(1, n + 1):
        base *= i
    print("Factorial:", base)

def imprimir_palabras_y_conteo():
    print("\n--- Imprimir palabras y contar ---")
    frase = input("Dame una frase: ")
    palabras = frase.split()
    for p in palabras:
        print(p)
    print("Total de palabras:", len(palabras))

def fibonacci_n():
    print("\n--- Serie Fibonacci (N términos) ---")
    n = int(input("Dime el valor de N: "))
    a, b = 0, 1
    for _ in range(n):
        print(b)
        a, b = b, a + b

def triangulo_asteriscos():
    print("\n--- Triángulo de asteriscos ---")
    num = int(input("Dime el número de * que quieres (altura): "))
    for i in range(0, num + 1):
        print("*" * i)

def suma_hasta_menos1():
    print("\n--- Suma números hasta teclear -1 ---")
    total = 0
    op = int(input("Dame un número (-1 para finalizar): "))
    while op != -1:
        total += op
        print("Suma parcial:", total)
        op = int(input("Dame un número (-1 para finalizar): "))
    print("Suma final:", total)

def pin_con_tres_intentos():
    print("\n--- PIN con 3 intentos ---")
    PIN_SECRETO = "1234"
    pin = input("Dame el PIN: ")
    intentos = 0
    while pin != PIN_SECRETO and intentos < 2:
        intentos += 1
        print(f"Pin incorrecto. Intentos: {intentos}. Vuelve a intentarlo...")
        pin = input("Dame el PIN: ")
    if pin == PIN_SECRETO:
        print("Desbloquear Pantalla")
    else:
        print("Llamando a @policia...")

def hipotenusa_validada():
    print("\n--- Hipotenusa con validación ---")
    c1 = float(input("Introduce el primer cateto (> 0): "))
    while c1 <= 0:
        print("El valor debe ser mayor a 0.")
        c1 = float(input("Introduce el primer cateto (> 0): "))
    c2 = float(input("Introduce el segundo cateto (> 0): "))
    while c2 <= 0:
        print("El valor debe ser mayor a 0.")
        c2 = float(input("Introduce el segundo cateto (> 0): "))
    h = math.sqrt(c1**2 + c2**2)
    print("La hipotenusa es:", h)

def calculadora_en_bucle():
    print("\n--- Calculadora en bucle (1, 2, 3 ó SAL) ---")
    operacion = input("Operación? Teclea 1, 2, 3 ó SAL: ").strip().upper()
    while operacion != "SAL":
        a = float(input("Dame el valor de A: "))
        b = float(input("Dame el valor de B: "))
        if operacion == "1":
            print("Resultado:", math.sqrt(a + b))
        elif operacion == "2":
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Error: división entre cero")
        elif operacion == "3":
            print("Resultado:", (a + b) / 2.5)
        else:
            print("Opción no válida.")
        operacion = input("Operación? Teclea 1, 2, 3 ó SAL: ").strip().upper()
    print("Saliendo de la calculadora...")

def combate_por_turnos():
    print("\n--- Combate por turnos ---")
    vidaA, ataqueA = 100, 20
    vidaB, ataqueB = 100, 20
    turno = random.randint(-1, 1) or 1  # asegura ±1

    while vidaA > 0 and vidaB > 0:
        if turno == 1:
            vidaA -= ataqueB
        else:
            vidaB -= ataqueA
        turno *= -1
        print(f"Vida de A: {vidaA} | Vida de B: {vidaB}")
        time.sleep(1.0)

    print("Ha ganado A" if vidaA > 0 else "Ha ganado B")

# Menú principal

def menu():
    while True:
        print("\n===== MENÚ DE OPCIONES (Bucles) =====")
        print("1. Contar del 1 al 10 (for)")
        print("2. Factorial de N (for)")
        print("3. Imprimir palabras y conteo (for)")
        print("4. Serie Fibonacci (for)")
        print("5. Triángulo de asteriscos (for)")
        print("6. Suma hasta -1 (while)")
        print("7. PIN con 3 intentos (while)")
        print("8. Hipotenusa validada (while)")
        print("9. Calculadora en bucle (while)")
        print("10. Combate por turnos (while)")
        print("0. Salir")

        op = input("Elige una opción: ").strip()
        if op == "1": contar_1_a_10()
        elif op == "2": factorial_n()
        elif op == "3": imprimir_palabras_y_conteo()
        elif op == "4": fibonacci_n()
        elif op == "5": triangulo_asteriscos()
        elif op == "6": suma_hasta_menos1()
        elif op == "7": pin_con_tres_intentos()
        elif op == "8": hipotenusa_validada()
        elif op == "9": calculadora_en_bucle()
        elif op == "10": combate_por_turnos()
        elif op == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
