"""
Actividad 1.2: Operadores en Python
Objetivo: Comprender y usar operadores aritméticos, de comparación y lógicos
"""

print("=== OPERADORES ARITMÉTICOS ===")

# Variables para trabajar
a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Suma: a + b = {a + b}")
print(f"Resta: a - b = {a - b}")
print(f"Multiplicación: a * b = {a * b}")
print(f"División: a / b = {a / b}")
print(f"División entera: a // b = {a // b}")
print(f"Módulo (residuo): a % b = {a % b}")
print(f"Potencia: a ** b = {a ** b}")

print("\n=== OPERADORES DE COMPARACIÓN ===")

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # Igualdad
print(f"x != y: {x != y}")  # Desigualdad
print(f"x < y: {x < y}")    # Menor que
print(f"x > y: {x > y}")    # Mayor que
print(f"x <= y: {x <= y}")  # Menor o igual
print(f"x >= y: {x >= y}")  # Mayor o igual

print("\n=== OPERADORES LÓGICOS ===")

p = True
q = False

print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")  # AND lógico
print(f"p or q: {p or q}")    # OR lógico
print(f"not p: {not p}")      # NOT lógico
print(f"not q: {not q}")

# Ejemplo práctico: Verificar si un estudiante aprueba
print("\n=== EJEMPLO PRÁCTICO: SISTEMA DE CALIFICACIONES ===")

calificacion = 85
asistencia = 90
tareas_completas = True

# Condiciones para aprobar
calificacion_minima = calificacion >= 70
asistencia_minima = asistencia >= 80
cumple_tareas = tareas_completas

aprueba = calificacion_minima and asistencia_minima and cumple_tareas

print(f"Calificación: {calificacion} (Mínimo 70): {calificacion_minima}")
print(f"Asistencia: {asistencia}% (Mínimo 80%): {asistencia_minima}")
print(f"Tareas completas: {cumple_tareas}")
print(f"¿Aprueba la materia?: {aprueba}")

# EJERCICIOS PARA EL ESTUDIANTE
print("\n=== EJERCICIOS ===")
print("1. Calcula el área de un rectángulo (largo * ancho)")
print("2. Verifica si un número es par (usa el operador %)")
print("3. Determina si una persona puede votar (edad >= 18)")

# ESPACIO PARA EJERCICIOS
# Ejercicio 1: Área de rectángulo
# largo = 5
# ancho = 3
# area = 

# Ejercicio 2: Verificar si un número es par
# numero = 8
# es_par = 

# Ejercicio 3: Verificar si puede votar
# edad_persona = 17
# puede_votar = 