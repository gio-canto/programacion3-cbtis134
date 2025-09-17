# =========================================
# Autor: Gio Antonio Canto Gomez
# Actividad: Variables y operaciones en Python
"""Descripción: presenta un menú de opciones para ejecutar ejercicios básicos:
 Hola Mundo, Variables básicas, Operaciones numéricas, Interés compuesto, Ley de Ohm,
 Circunferencia y diámetro, Peso molecular, Predicción de precio de casa y Marketing CTR. 
 Las “funciones” se representan como secciones simuladas conforme al estándar.
 #opcion: carácter {Opción del menú seleccionada por el usuario}"""

import math

def saludo():
    print("\n--- Ejemplo Hola Mundo ---")
    print("Hola Mundo!")

def variables_basicas():
    print("\n--- Variables y tipos básicos ---")
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    precio = float(input("Introduce un precio: "))
    es_estudiante = input("¿Eres estudiante? (si/no): ").lower() == "si"

    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Precio:", precio)
    print("¿Es estudiante?:", es_estudiante)

def operaciones_numericas():
    print("\n--- Operaciones numéricas ---")
    numero = int(input("Introduce un número entero: "))
    resultado = numero * 2
    print("Multiplicado por 2:", resultado)
    print("Dividido entre 1.5:", resultado / 1.5)

def interes_compuesto():
    print("\n--- Interés compuesto ---")
    capital = float(input("Capital inicial: "))
    interes = float(input("Interés anual (ej. 0.02): "))
    años = int(input("Número de años: "))
    acumulado = capital * (1 + interes) ** años
    print("Valor acumulado:", acumulado)
    print("Intereses obtenidos:", acumulado - capital)

def ley_ohm():
    print("\n--- Ley de Ohm (V = I * R) ---")
    intensidad = float(input("Intensidad (A): "))
    resistencia = float(input("Resistencia (Ω): "))
    voltaje = intensidad * resistencia
    print("Voltaje calculado:", voltaje, "V")

def circunferencia():
    print("\n--- Circunferencia y diámetro ---")
    radio = float(input("Radio del círculo: "))
    circ = 2 * math.pi * radio
    diam = 2 * radio
    print("Circunferencia:", circ)
    print("Diámetro:", diam)

def peso_molecular():
    print("\n--- Peso molecular ---")
    peso1 = float(input("Peso del primer átomo: "))
    atomo1 = int(input("Número de átomos del primero: "))
    peso2 = float(input("Peso del segundo átomo: "))
    atomo2 = int(input("Número de átomos del segundo: "))
    resultado = peso1 * atomo1 + peso2 * atomo2
    print("Peso molecular:", resultado)

def prediccion_casa():
    print("\n--- Predicción de precio de casa ---")
    metros = float(input("Metros de la casa: "))
    habitaciones = int(input("Número de habitaciones: "))
    prediccion = metros * 804 + 1200.35 * habitaciones + 7000.5
    print("Precio estimado:", prediccion, "€")

def marketing_ctr():
    print("\n--- Marketing: CTR ---")
    impresiones = int(input("Número de impresiones: "))
    clicks = int(input("Número de clics: "))
    ctr = (clicks / impresiones) * 100
    print("CTR de la campaña:", ctr, "%")

# Menú principal

while True:
    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Hola Mundo")
    print("2. Variables básicas")
    print("3. Operaciones numéricas")
    print("4. Interés compuesto")
    print("5. Ley de Ohm")
    print("6. Circunferencia y diámetro")
    print("7. Peso molecular")
    print("8. Predicción precio casa")
    print("9. Marketing CTR")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1": saludo()
    elif opcion == "2": variables_basicas()
    elif opcion == "3": operaciones_numericas()
    elif opcion == "4": interes_compuesto()
    elif opcion == "5": ley_ohm()
    elif opcion == "6": circunferencia()
    elif opcion == "7": peso_molecular()
    elif opcion == "8": prediccion_casa()
    elif opcion == "9": marketing_ctr()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")

