"""
Actividad 1.3: Conversiones de Tipo de Datos
Objetivo: Aprender a convertir entre diferentes tipos de datos
"""

print("=== CONVERSIONES DE TIPOS DE DATOS ===")

# CONVERSIÓN A ENTERO (int)
print("=== Conversión a int() ===")
texto_numero = "25"
decimal = 15.75
booleano = True

print(f"Texto '{texto_numero}' a int: {int(texto_numero)}")
print(f"Decimal {decimal} a int: {int(decimal)}")  # Trunca la parte decimal
print(f"Booleano {booleano} a int: {int(booleano)}")  # True = 1, False = 0

# CONVERSIÓN A DECIMAL (float)
print("\n=== Conversión a float() ===")
numero_entero = 42
texto_decimal = "3.14"
booleano_false = False

print(f"Entero {numero_entero} a float: {float(numero_entero)}")
print(f"Texto '{texto_decimal}' a float: {float(texto_decimal)}")
print(f"Booleano {booleano_false} a float: {float(booleano_false)}")

# CONVERSIÓN A TEXTO (str)
print("\n=== Conversión a str() ===")
numero = 100
decimal_num = 98.6
es_verdadero = True

print(f"Número {numero} a str: '{str(numero)}'")
print(f"Decimal {decimal_num} a str: '{str(decimal_num)}'")
print(f"Booleano {es_verdadero} a str: '{str(es_verdadero)}'")

# CONVERSIÓN A BOOLEANO (bool)
print("\n=== Conversión a bool() ===")
numero_positivo = 5
numero_cero = 0
texto_vacio = ""
texto_lleno = "Hola"

print(f"Número positivo {numero_positivo} a bool: {bool(numero_positivo)}")
print(f"Número cero {numero_cero} a bool: {bool(numero_cero)}")
print(f"Texto vacío '{texto_vacio}' a bool: {bool(texto_vacio)}")
print(f"Texto '{texto_lleno}' a bool: {bool(texto_lleno)}")

# EJEMPLO PRÁCTICO: CALCULADORA SIMPLE
print("\n=== EJEMPLO PRÁCTICO: CALCULADORA ===")

# Simulamos entrada del usuario (normalmente usaríamos input())
entrada1 = "10"
entrada2 = "3.5"
operacion = "+"

# Convertimos las entradas a números
num1 = float(entrada1)
num2 = float(entrada2)

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2
else:
    resultado = "Operación no válida"

print(f"{entrada1} {operacion} {entrada2} = {resultado}")

# MANEJO DE ERRORES EN CONVERSIONES
print("\n=== MANEJO DE ERRORES ===")

# Estas conversiones causarían error si no las manejamos
try:
    texto_invalido = "abc"
    numero_invalido = int(texto_invalido)  # Esto causaría error
except ValueError:
    print(f"Error: No se puede convertir '{texto_invalido}' a número")

try:
    division_por_cero = 10 / 0  # Esto causaría error
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")

# EJERCICIOS PARA EL ESTUDIANTE
print("\n=== EJERCICIOS ===")
print("1. Convierte tu edad (string) a número para hacer cálculos")
print("2. Convierte el resultado de una división a entero")
print("3. Verifica qué valores se consideran False al convertir a bool")

# ESPACIO PARA EJERCICIOS
# Ejercicio 1: Conversión de edad
# edad_texto = "16"
# edad_numero = 
# año_nacimiento = 2024 - edad_numero

# Ejercicio 2: División y conversión
# dividendo = 17
# divisor = 3
# cociente_entero = 

# Ejercicio 3: Valores que se convierten a False
# valores_prueba = [0, "", [], None, False]
# for valor in valores_prueba:
#     print(f"{valor} a bool: {bool(valor)}")