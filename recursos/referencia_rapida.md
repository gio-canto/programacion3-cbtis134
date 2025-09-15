# 🐍 Python Quick Reference - CBTIS 3er Semestre

## Tipos de Datos Básicos
```python
# Números
entero = 42
decimal = 3.14

# Texto
nombre = "Juan"
mensaje = 'Hola mundo'

# Booleanos
verdadero = True
falso = False
```

## Operadores
```python
# Aritméticos
suma = 5 + 3        # 8
resta = 5 - 3       # 2
multiplicacion = 5 * 3   # 15
division = 5 / 3    # 1.666...
division_entera = 5 // 3  # 1
modulo = 5 % 3      # 2
potencia = 5 ** 3   # 125

# Comparación
igual = 5 == 5      # True
diferente = 5 != 3  # True
mayor = 5 > 3       # True
menor = 5 < 3       # False

# Lógicos
y_logico = True and False    # False
o_logico = True or False     # True
negacion = not True          # False
```

## Entrada y Salida
```python
# Mostrar en pantalla
print("Hola mundo")
print(f"Mi nombre es {nombre}")

# Capturar del usuario
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
```

## Condicionales
```python
# if simple
if edad >= 18:
    print("Eres mayor de edad")

# if-else
if calificacion >= 70:
    print("Aprobaste")
else:
    print("Reprobaste")

# if-elif-else
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bien")
elif calificacion >= 70:
    print("Bien")
else:
    print("Necesitas mejorar")
```

## Bucles
```python
# for con range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# for con listas
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

## Listas
```python
# Crear listas
vacia = []
numeros = [1, 2, 3, 4, 5]
mixta = ["texto", 42, True]

# Acceder elementos
primer_elemento = numeros[0]    # 1
ultimo_elemento = numeros[-1]   # 5

# Métodos importantes
numeros.append(6)               # Agregar al final
numeros.insert(0, 0)           # Insertar en posición
numeros.remove(3)              # Eliminar por valor
elemento = numeros.pop()        # Eliminar y retornar último
numeros.sort()                 # Ordenar
cantidad = len(numeros)        # Longitud
```

## Funciones
```python
# Función simple
def saludar():
    print("¡Hola!")

# Función con parámetros
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

# Función con return
def sumar(a, b):
    resultado = a + b
    return resultado

# Función con parámetro por defecto
def potencia(base, exponente=2):
    return base ** exponente

# Usar funciones
saludar()
saludar_persona("María")
resultado = sumar(5, 3)
cuadrado = potencia(4)      # usa exponente=2 por defecto
cubo = potencia(4, 3)
```

## Diccionarios
```python
# Crear diccionario
estudiante = {
    "nombre": "Ana",
    "edad": 17,
    "semestre": 3
}

# Acceder valores
nombre = estudiante["nombre"]
edad = estudiante.get("edad", 0)    # Con valor por defecto

# Modificar
estudiante["edad"] = 18
estudiante["promedio"] = 8.5

# Métodos útiles
claves = estudiante.keys()
valores = estudiante.values()
items = estudiante.items()
```

## Manejo de Errores
```python
# try-except básico
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
```

## Comprensiones de Listas
```python
# Lista de cuadrados
cuadrados = [x**2 for x in range(5)]    # [0, 1, 4, 9, 16]

# Lista con condición
pares = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]
```

## Funciones Built-in Útiles
```python
# Matemáticas
maximo = max([1, 5, 3, 9, 2])    # 9
minimo = min([1, 5, 3, 9, 2])    # 1
suma_total = sum([1, 2, 3, 4])   # 10
absoluto = abs(-5)               # 5

# Conversiones
entero = int("42")
decimal = float("3.14")
texto = str(42)

# Otros
longitud = len("Hola")           # 4
ordenada = sorted([3, 1, 4, 1])  # [1, 1, 3, 4]
```

## Strings (Cadenas)
```python
texto = "Hola Mundo"

# Métodos útiles
mayusculas = texto.upper()       # "HOLA MUNDO"
minusculas = texto.lower()       # "hola mundo"
sin_espacios = texto.strip()     # quita espacios al inicio/final
reemplazar = texto.replace("Hola", "Hi")  # "Hi Mundo"

# Verificaciones
empieza_con = texto.startswith("Hola")    # True
termina_con = texto.endswith("Mundo")     # True
es_numero = "123".isdigit()               # True
```

## Consejos Rápidos
- **Indentación**: Usa 4 espacios para indentar
- **Nombres**: snake_case para variables y funciones
- **Comentarios**: Usa # para comentarios de una línea
- **Docstrings**: Usa """texto""" para documentar funciones
- **PEP 8**: Guía de estilo oficial de Python

## Errores Comunes
```python
# ❌ Error de indentación
if True:
print("Error")

# ✅ Correcto
if True:
    print("Correcto")

# ❌ Comparación vs asignación
if x = 5:  # Error, usar ==

# ✅ Correcto
if x == 5:
    print("x es 5")
```