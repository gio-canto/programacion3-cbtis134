"""
Actividad 3.1: Estructuras Condicionales
Objetivo: Dominar el uso de if, elif y else para tomar decisiones
"""

print("=== ESTRUCTURAS CONDICIONALES ===")

# CONDICIONAL SIMPLE (if)
print("=== 1. CONDICIONAL SIMPLE ===")
edad = 18

if edad >= 18:
    print(f"Edad: {edad} - Eres mayor de edad")

if edad < 18:
    print(f"Edad: {edad} - Eres menor de edad")

# CONDICIONAL CON ELSE
print("\n=== 2. CONDICIONAL IF-ELSE ===")
calificacion = 75

if calificacion >= 70:
    print(f"Calificación: {calificacion} - ¡Aprobaste!")
else:
    print(f"Calificación: {calificacion} - Necesitas estudiar más")

# CONDICIONAL MÚLTIPLE (elif)
print("\n=== 3. CONDICIONAL IF-ELIF-ELSE ===")
temperatura = 25

if temperatura > 30:
    print(f"{temperatura}°C - Hace mucho calor")
elif temperatura > 20:
    print(f"{temperatura}°C - Temperatura agradable")
elif temperatura > 10:
    print(f"{temperatura}°C - Hace frío")
else:
    print(f"{temperatura}°C - Hace mucho frío")

# CONDICIONES COMPUESTAS
print("\n=== 4. CONDICIONES COMPUESTAS ===")
hora = 14
dia_semana = "lunes"

if hora >= 8 and hora <= 15 and dia_semana != "sábado" and dia_semana != "domingo":
    print("Es horario de clases")
else:
    print("No es horario de clases")

# EJEMPLO PRÁCTICO: SISTEMA DE CALIFICACIONES
print("\n=== EJEMPLO PRÁCTICO: SISTEMA DE CALIFICACIONES ===")

def evaluar_estudiante(calificacion, asistencia, tareas):
    """Evalúa si un estudiante aprueba basado en múltiples criterios"""
    
    print(f"\nEvaluando estudiante:")
    print(f"Calificación: {calificacion}")
    print(f"Asistencia: {asistencia}%")
    print(f"Tareas entregadas: {tareas}%")
    
    # Verificar condiciones de aprobación
    if calificacion >= 90 and asistencia >= 90 and tareas >= 90:
        resultado = "EXCELENTE - Felicitaciones"
    elif calificacion >= 80 and asistencia >= 85 and tareas >= 80:
        resultado = "MUY BIEN - Aprobado"
    elif calificacion >= 70 and asistencia >= 80 and tareas >= 70:
        resultado = "BIEN - Aprobado"
    elif calificacion >= 60:
        if asistencia < 70:
            resultado = "REPROBADO - Falta de asistencia"
        elif tareas < 60:
            resultado = "REPROBADO - Tareas incompletas"
        else:
            resultado = "EXTRAORDINARIO - Última oportunidad"
    else:
        resultado = "REPROBADO - Calificación insuficiente"
    
    print(f"Resultado: {resultado}")
    return resultado

# Probar con diferentes estudiantes
evaluar_estudiante(95, 98, 100)
evaluar_estudiante(82, 88, 85)
evaluar_estudiante(68, 65, 80)
evaluar_estudiante(55, 90, 90)

# OPERADOR TERNARIO (CONDICIONAL EN UNA LÍNEA)
print("\n=== 5. OPERADOR TERNARIO ===")
edad_persona = 20
mensaje = "Mayor de edad" if edad_persona >= 18 else "Menor de edad"
print(f"Edad: {edad_persona} - {mensaje}")

# Más ejemplos de operador ternario
numero = 15
paridad = "Par" if numero % 2 == 0 else "Impar"
print(f"El número {numero} es {paridad}")

# VALIDACIÓN DE DATOS
print("\n=== 6. VALIDACIÓN DE DATOS ===")

def validar_calificacion(cal):
    """Valida que una calificación esté en el rango correcto"""
    if cal < 0:
        return "Error: La calificación no puede ser negativa"
    elif cal > 100:
        return "Error: La calificación no puede ser mayor a 100"
    elif cal >= 70:
        return "Aprobado"
    else:
        return "Reprobado"

# Probar validación
calificaciones_prueba = [-5, 85, 150, 65, 95]
for cal in calificaciones_prueba:
    resultado = validar_calificacion(cal)
    print(f"Calificación {cal}: {resultado}")

# EJERCICIOS PARA EL ESTUDIANTE
print("\n=== EJERCICIOS ===")
print("1. Crea un programa que determine si un año es bisiesto")
print("2. Implementa un sistema de descuentos por edad")
print("3. Crea un clasificador de películas por edad")

# PLANTILLAS PARA EJERCICIOS
"""
# Ejercicio 1: Año bisiesto
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100,
# a menos que también sea divisible por 400
# año = 2024
# if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#     print(f"{año} es bisiesto")
# else:
#     print(f"{año} no es bisiesto")

# Ejercicio 2: Sistema de descuentos
# edad_cliente = 25
# precio_original = 100
# if edad_cliente < 12:
#     descuento = 0.5  # 50% para niños
# elif edad_cliente >= 65:
#     descuento = 0.3  # 30% para adultos mayores
# elif edad_cliente < 18:
#     descuento = 0.2  # 20% para estudiantes
# else:
#     descuento = 0    # Sin descuento
# precio_final = precio_original * (1 - descuento)

# Ejercicio 3: Clasificación de películas
# edad_espectador = 16
# clasificacion_pelicula = "R"  # G, PG, PG-13, R
# if clasificacion_pelicula == "G":
#     print("Apta para toda la familia")
# elif clasificacion_pelicula == "PG" and edad_espectador >= 8:
#     print("Recomendada supervisión parental")
# elif clasificacion_pelicula == "PG-13" and edad_espectador >= 13:
#     print("No recomendada para menores de 13")
# elif clasificacion_pelicula == "R" and edad_espectador >= 17:
#     print("Solo para mayores de 17")
# else:
#     print("No puedes ver esta película")
"""