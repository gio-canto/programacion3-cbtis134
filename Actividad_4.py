"""
=========================================
Autor: Gio Antonio Canto Gómez
Actividad: Condicionales en Python
Descripción: Este programa presenta un menú de opciones con ejercicios de condicionales:
    - Comparar números
    - Verificar edad
    - Calcular hipotenusa
    - Operaciones básicas
    - Descuento por puntos
    - Calcular factura
    - Verificar contraseña
    - Determinar año bisiesto
    - Tarifa especial
    - Pizza personalizada
"""

import math

def comparar_numeros():
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))
    if a > b:
        print("a es mayor que b")
    else:
        print("a no es mayor que b")

def verificar_edad():
    edad = int(input("¿Qué edad tienes? "))
    if edad >= 18:
        print("Puedes pasar :D")
    else:
        print("Lo siento. No puedes pasar...")

def calcular_hipotenusa():
    c1 = float(input("Introduce el primer cateto: "))
    c2 = float(input("Introduce el segundo cateto: "))
    if c1 <= 0 or c2 <= 0:
        print("Error: los catetos deben ser positivos.")
    else:
        h = math.sqrt(c1**2 + c2**2)
        print("La hipotenusa es:", h)

def operaciones_basicas():
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    op = int(input("Operación [1: Suma / 2: Multiplica / 3: Resta / 4: Divide]: "))
    if op == 1:
        print("Resultado:", a + b)
    elif op == 2:
        print("Resultado:", a * b)
    elif op == 3:
        print("Resultado:", a - b)
    else:
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Error: división entre cero")

def descuento_puntos():
    precio = float(input("Introduce el precio de la compra: "))
    puntos = int(input("Introduce los puntos del cliente: "))
    if puntos < 100:
        precio *= 0.9
    elif 100 < puntos < 150:
        precio *= 0.88
    elif puntos == 150:
        precio *= 0.85
    elif puntos > 150:
        precio *= 0.8
    print("Precio final con descuento:", precio)

def calcular_factura():
    base = float(input("Introduce la base de la factura: "))
    tipo = input("Tipo de factura [H: Hostelería / N: Normal]: ")
    if tipo == "H":
        total = base * 1.1
    else:
        total = base * 1.21
    print("Total a pagar:", total)

def verificar_password():
    password = "1234"
    intento = input("Introduce la contraseña: ")
    if intento == password:
        print("Bienvenid@")
    else:
        print("Contraseña incorrecta. Ordenador bloqueado.")

def anio_bisiesto():
    ano = int(input("Introduce un año: "))
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print("Es bisiesto")
            else:
                print("No es bisiesto")
        else:
            print("Es bisiesto")
    else:
        print("No es bisiesto")

def tarifa_especial():
    tarifa = float(input("Introduce la tarifa anual: "))
    edad = int(input("Introduce tu edad: "))
    trabaja = input("¿Trabajas? (si/no): ")
    if edad < 18 and trabaja == "no":
        tarifa *= 0.5
    elif edad >= 18 and trabaja == "no":
        tarifa *= 0.75
    elif edad < 18 and trabaja == "si":
        tarifa *= 0.95
    print("Tarifa final:", tarifa)

def pizza():
    tipo_pizza = input("¿Quieres pizza vegetariana? (si/no): ")
    if tipo_pizza == "si":
        print("Ingredientes vegetarianos: 1. Pimiento 2. Tofu")
        opcion = int(input("Elige ingrediente (1 o 2): "))
        ingrediente = "Pimiento" if opcion == 1 else "Tofu"
        tipo = "vegetariana"
    else:
        print("Ingredientes no vegetarianos: 1. Peperoni 2. Jamón 3. Salmón")
        opcion = int(input("Elige ingrediente (1, 2 o 3): "))
        if opcion == 1:
            ingrediente = "Peperoni"
        elif opcion == 2:
            ingrediente = "Jamón"
        else:
            ingrediente = "Salmón"
        tipo = "no vegetariana"
    print("Has elegido una pizza", tipo, "con mozzarella, tomate y", ingrediente)


# Menú principal

while True:
    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Comparar números")
    print("2. Verificar edad")
    print("3. Calcular hipotenusa")
    print("4. Operaciones básicas")
    print("5. Descuento por puntos")
    print("6. Calcular factura")
    print("7. Verificar contraseña")
    print("8. Año bisiesto")
    print("9. Tarifa especial")
    print("10. Pizza personalizada")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1": comparar_numeros()
    elif opcion == "2": verificar_edad()
    elif opcion == "3": calcular_hipotenusa()
    elif opcion == "4": operaciones_basicas()
    elif opcion == "5": descuento_puntos()
    elif opcion == "6": calcular_factura()
    elif opcion == "7": verificar_password()
    elif opcion == "8": anio_bisiesto()
    elif opcion == "9": tarifa_especial()
    elif opcion == "10": pizza()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
