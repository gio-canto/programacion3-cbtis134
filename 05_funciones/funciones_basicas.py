"""
Actividad 5.1: Funciones en Python
Objetivo: Aprender a crear y usar funciones para organizar el código
"""

print("=== FUNCIONES EN PYTHON ===")

# FUNCIONES BÁSICAS
print("=== 1. FUNCIONES BÁSICAS ===")

def saludar():
    """Función simple que saluda"""
    print("¡Hola desde una función!")

def saludar_personalizado(nombre):
    """Función con parámetro"""
    print(f"¡Hola, {nombre}!")

def saludar_completo(nombre, apellido=""):
    """Función con parámetro opcional"""
    if apellido:
        print(f"¡Hola, {nombre} {apellido}!")
    else:
        print(f"¡Hola, {nombre}!")

# Usar las funciones
saludar()
saludar_personalizado("María")
saludar_completo("Juan", "Pérez")
saludar_completo("Ana")

# FUNCIONES QUE RETORNAN VALORES
print("\n=== 2. FUNCIONES CON RETURN ===")

def sumar(a, b):
    """Suma dos números y retorna el resultado"""
    resultado = a + b
    return resultado

def calcular_promedio(calificaciones):
    """Calcula el promedio de una lista de calificaciones"""
    if not calificaciones:  # Lista vacía
        return 0
    
    suma_total = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = suma_total / cantidad
    return promedio

def es_aprobatorio(calificacion):
    """Determina si una calificación es aprobatoria"""
    return calificacion >= 70

# Usar funciones con return
resultado_suma = sumar(15, 25)
print(f"15 + 25 = {resultado_suma}")

mis_calificaciones = [85, 92, 78, 96, 88]
mi_promedio = calcular_promedio(mis_calificaciones)
print(f"Calificaciones: {mis_calificaciones}")
print(f"Promedio: {mi_promedio:.2f}")
print(f"¿Aprobatorio?: {es_aprobatorio(mi_promedio)}")

# FUNCIONES CON MÚLTIPLES PARÁMETROS
print("\n=== 3. FUNCIONES CON MÚLTIPLES PARÁMETROS ===")

def calcular_bmi(peso, altura, unidad_peso="kg"):
    """
    Calcula el Índice de Masa Corporal
    peso: peso en kg o libras
    altura: altura en metros
    unidad_peso: 'kg' o 'lb'
    """
    if unidad_peso == "lb":
        peso = peso * 0.453592  # Convertir libras a kg
    
    bmi = peso / (altura ** 2)
    return bmi

def clasificar_bmi(bmi):
    """Clasifica el BMI según estándares médicos"""
    if bmi < 18.5:
        return "Bajo peso"
    elif bmi < 25:
        return "Peso normal"
    elif bmi < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Ejemplo de uso
peso_persona = 70  # kg
altura_persona = 1.75  # metros

bmi_calculado = calcular_bmi(peso_persona, altura_persona)
clasificacion = clasificar_bmi(bmi_calculado)

print(f"Peso: {peso_persona} kg")
print(f"Altura: {altura_persona} m")
print(f"BMI: {bmi_calculado:.2f}")
print(f"Clasificación: {clasificacion}")

# FUNCIONES CON ARGUMENTOS VARIABLES
print("\n=== 4. ARGUMENTOS VARIABLES ===")

def sumar_varios(*numeros):
    """Suma cualquier cantidad de números"""
    total = 0
    for numero in numeros:
        total += numero
    return total

def mostrar_info_estudiante(nombre, **datos):
    """Muestra información del estudiante con datos variables"""
    print(f"\nEstudiante: {nombre}")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# Usar argumentos variables
print(f"Suma de 1, 2, 3: {sumar_varios(1, 2, 3)}")
print(f"Suma de 10, 20, 30, 40, 50: {sumar_varios(10, 20, 30, 40, 50)}")

mostrar_info_estudiante("Ana García", 
                       edad=17, 
                       semestre=3, 
                       promedio=8.5, 
                       escuela="CBTIS")

# FUNCIONES COMO HERRAMIENTAS DE CÁLCULO
print("\n=== 5. CALCULADORA CON FUNCIONES ===")

def menu_calculadora():
    """Muestra el menú de la calculadora"""
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("0. Salir")

def sumar_calc(a, b):
    return a + b

def restar_calc(a, b):
    return a - b

def multiplicar_calc(a, b):
    return a * b

def dividir_calc(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia_calc(base, exponente):
    return base ** exponente

def raiz_cuadrada_calc(numero):
    if numero < 0:
        return "Error: No se puede calcular raíz de número negativo"
    return numero ** 0.5

def calculadora_interactiva():
    """Calculadora interactiva usando funciones"""
    print("🧮 CALCULADORA INTERACTIVA")
    
    # Ejemplo de operaciones sin interacción del usuario
    print("\n--- EJEMPLOS DE OPERACIONES ---")
    print(f"10 + 5 = {sumar_calc(10, 5)}")
    print(f"10 - 5 = {restar_calc(10, 5)}")
    print(f"10 * 5 = {multiplicar_calc(10, 5)}")
    print(f"10 / 5 = {dividir_calc(10, 5)}")
    print(f"2 ^ 8 = {potencia_calc(2, 8)}")
    print(f"√25 = {raiz_cuadrada_calc(25)}")
    
    # Ejemplo de error
    print(f"10 / 0 = {dividir_calc(10, 0)}")
    print(f"√(-4) = {raiz_cuadrada_calc(-4)}")

calculadora_interactiva()

# FUNCIONES PARA GESTIÓN ESCOLAR
print("\n=== 6. SISTEMA DE GESTIÓN ESCOLAR ===")

def calcular_calificacion_final(parciales, tareas, proyecto, examen_final):
    """
    Calcula la calificación final basada en diferentes componentes
    parciales: lista de calificaciones parciales (30%)
    tareas: calificación promedio de tareas (20%)
    proyecto: calificación del proyecto (25%)
    examen_final: calificación del examen final (25%)
    """
    
    # Calcular promedio de parciales
    promedio_parciales = sum(parciales) / len(parciales)
    
    # Calcular calificación final ponderada
    calificacion_final = (
        promedio_parciales * 0.30 +
        tareas * 0.20 +
        proyecto * 0.25 +
        examen_final * 0.25
    )
    
    return calificacion_final

def generar_reporte_estudiante(nombre, parciales, tareas, proyecto, examen_final):
    """Genera un reporte completo del estudiante"""
    calificacion_final = calcular_calificacion_final(parciales, tareas, proyecto, examen_final)
    
    print(f"\n📊 REPORTE DE {nombre.upper()}")
    print("-" * 40)
    print(f"Parciales: {parciales} (Promedio: {sum(parciales)/len(parciales):.1f})")
    print(f"Tareas: {tareas}")
    print(f"Proyecto: {proyecto}")
    print(f"Examen Final: {examen_final}")
    print("-" * 40)
    print(f"CALIFICACIÓN FINAL: {calificacion_final:.2f}")
    
    if calificacion_final >= 90:
        print("🏆 EXCELENTE")
    elif calificacion_final >= 80:
        print("⭐ MUY BIEN")
    elif calificacion_final >= 70:
        print("👍 APROBADO")
    else:
        print("❌ REPROBADO")
    
    return calificacion_final

# Ejemplo de uso del sistema
estudiantes_ejemplo = [
    ("María González", [85, 90, 88], 92, 87, 89),
    ("Juan Pérez", [78, 82, 75], 85, 90, 88),
    ("Ana López", [95, 93, 97], 98, 95, 94)
]

print("🎓 REPORTES DE LA CLASE")
for datos in estudiantes_ejemplo:
    nombre, parciales, tareas, proyecto, examen = datos
    generar_reporte_estudiante(nombre, parciales, tareas, proyecto, examen)

# EJERCICIOS PARA EL ESTUDIANTE
print("\n=== EJERCICIOS ===")
print("1. Crea una función que convierta temperaturas (C a F y viceversa)")
print("2. Implementa una función que valide si un año es bisiesto")
print("3. Crea un conversor de unidades (metros a pies, kg a libras, etc.)")

# PLANTILLAS PARA EJERCICIOS
"""
# Ejercicio 1: Conversor de temperatura
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Ejercicio 2: Año bisiesto
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Ejercicio 3: Conversor de unidades
def metros_a_pies(metros):
    return metros * 3.28084

def kg_a_libras(kg):
    return kg * 2.20462
"""