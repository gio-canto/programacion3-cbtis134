"""
Actividad 2.1: Entrada de Datos del Usuario
Objetivo: Aprender a capturar y procesar datos ingresados por el usuario
"""

print("=== BIENVENIDO AL SISTEMA DE REGISTRO DE ESTUDIANTES ===")

# CAPTURA DE DATOS BÁSICOS
print("\nPor favor, ingresa la siguiente información:")

# Captura de datos de texto
nombre = input("Nombre: ")
apellido = input("Apellido: ")
escuela = input("Nombre de tu escuela: ")

# Captura de datos numéricos (hay que convertir)
edad_texto = input("Edad: ")
edad = int(edad_texto)  # Convertimos a entero

semestre_texto = input("Semestre que cursas: ")
semestre = int(semestre_texto)

# Captura de datos decimales
promedio_texto = input("Tu promedio actual: ")
promedio = float(promedio_texto)

# PROCESAMIENTO DE DATOS
print("\n" + "="*50)
print("INFORMACIÓN REGISTRADA")
print("="*50)

# Mostrar información formateada
print(f"Estudiante: {nombre} {apellido}")
print(f"Escuela: {escuela}")
print(f"Edad: {edad} años")
print(f"Semestre: {semestre}")
print(f"Promedio: {promedio}")

# Cálculos basados en los datos
año_actual = 2024
año_nacimiento = año_actual - edad
print(f"Año de nacimiento aproximado: {año_nacimiento}")

# Validaciones simples
if promedio >= 9.0:
    nivel_academico = "Excelente"
elif promedio >= 8.0:
    nivel_academico = "Muy bueno"
elif promedio >= 7.0:
    nivel_academico = "Bueno"
else:
    nivel_academico = "Necesita mejorar"

print(f"Nivel académico: {nivel_academico}")

# EJEMPLO AVANZADO: CAPTURA CON VALIDACIÓN
print("\n=== EJEMPLO CON VALIDACIÓN ===")

# Función para capturar un número con validación
def capturar_numero(mensaje):
    while True:
        try:
            valor = input(mensaje)
            numero = float(valor)
            return numero
        except ValueError:
            print("Error: Ingresa un número válido")

# Uso de la función de validación
print("Ingresa las calificaciones de 3 materias:")
cal1 = capturar_numero("Calificación 1: ")
cal2 = capturar_numero("Calificación 2: ")
cal3 = capturar_numero("Calificación 3: ")

promedio_materias = (cal1 + cal2 + cal3) / 3
print(f"\nPromedio de las 3 materias: {promedio_materias:.2f}")

# EJERCICIOS PARA EL ESTUDIANTE
print("\n=== EJERCICIOS ===")
print("1. Crea un programa que capture datos de tu familia")
print("2. Calcula la edad de cada miembro en el año 2030")
print("3. Determina quién es mayor y menor de edad")

# PLANTILLA PARA EJERCICIOS
"""
# Ejercicio 1: Datos familiares
# nombre_padre = input("Nombre del padre: ")
# edad_padre = int(input("Edad del padre: "))
# ... continúa con más familiares

# Ejercicio 2: Edades en 2030
# edad_padre_2030 = edad_padre + (2030 - 2024)

# Ejercicio 3: Verificación mayoría de edad
# es_mayor_padre = edad_padre >= 18
"""