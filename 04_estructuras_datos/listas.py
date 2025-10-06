"""
Actividad 4.1: Trabajando con Listas
Objetivo: Dominar la creación y manipulación de listas en Python
"""

print("=== TRABAJANDO CON LISTAS ===")

# CREACIÓN DE LISTAS
print("=== 1. CREACIÓN DE LISTAS ===")

# Lista vacía
lista_vacia = []
print(f"Lista vacía: {lista_vacia}")

# Lista con elementos
calificaciones = [85, 92, 78, 96, 88]
print(f"Calificaciones: {calificaciones}")

# Lista con diferentes tipos de datos
estudiante = ["María", "González", 17, True, 9.5]
print(f"Datos del estudiante: {estudiante}")

# Lista con números del 1 al 10
numeros = list(range(1, 11))
print(f"Números 1-10: {numeros}")

# ACCESO A ELEMENTOS
print("\n=== 2. ACCESO A ELEMENTOS ===")

materias = ["Matemáticas", "Física", "Química", "Biología", "Historia"]
print(f"Lista de materias: {materias}")

# Acceso por índice
print(f"Primera materia: {materias[0]}")
print(f"Última materia: {materias[-1]}")
print(f"Segunda materia: {materias[1]}")

# Slicing (rebanadas)
print(f"Primeras 3 materias: {materias[0:3]}")
print(f"Últimas 2 materias: {materias[-2:]}")
print(f"Materias del 2 al 4: {materias[1:4]}")

# MODIFICACIÓN DE LISTAS
print("\n=== 3. MODIFICACIÓN DE LISTAS ===")

frutas = ["manzana", "banana", "naranja"]
print(f"Lista original: {frutas}")

# Cambiar un elemento
frutas[1] = "pera"
print(f"Después de cambiar banana por pera: {frutas}")

# Agregar elementos
frutas.append("uva")  # Al final
print(f"Después de agregar uva: {frutas}")

frutas.insert(1, "kiwi")  # En posición específica
print(f"Después de insertar kiwi en posición 1: {frutas}")

# Extender la lista
frutas_tropicales = ["mango", "piña"]
frutas.extend(frutas_tropicales)
print(f"Después de extender con frutas tropicales: {frutas}")

# ELIMINACIÓN DE ELEMENTOS
print("\n=== 4. ELIMINACIÓN DE ELEMENTOS ===")

numeros_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista original: {numeros_ejemplo}")

# Eliminar por valor
numeros_ejemplo.remove(5)  # Remueve el primer 5 que encuentre
print(f"Después de remove(5): {numeros_ejemplo}")

# Eliminar por índice
elemento_eliminado = numeros_ejemplo.pop(2)  # Elimina y retorna
print(f"Eliminamos el elemento en índice 2: {elemento_eliminado}")
print(f"Lista después del pop: {numeros_ejemplo}")

# Eliminar el último elemento
ultimo = numeros_ejemplo.pop()
print(f"Último elemento eliminado: {ultimo}")
print(f"Lista final: {numeros_ejemplo}")

# MÉTODOS ÚTILES DE LISTAS
print("\n=== 5. MÉTODOS ÚTILES ===")

puntuaciones = [88, 92, 76, 88, 95, 88, 82]
print(f"Puntuaciones originales: {puntuaciones}")

# Contar elementos
print(f"Cantidad de 88: {puntuaciones.count(88)}")

# Encontrar índice
print(f"Índice de 95: {puntuaciones.index(95)}")

# Ordenar
puntuaciones_copia = puntuaciones.copy()  # Hacer una copia
puntuaciones_copia.sort()  # Ordenar ascendente
print(f"Ordenadas ascendente: {puntuaciones_copia}")

puntuaciones_copia.sort(reverse=True)  # Ordenar descendente
print(f"Ordenadas descendente: {puntuaciones_copia}")

# Revertir
lista_numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {lista_numeros}")
lista_numeros.reverse()
print(f"Lista revertida: {lista_numeros}")

# LISTAS ANIDADAS (MATRICES)
print("\n=== 6. LISTAS ANIDADAS ===")

# Calificaciones por materia para 3 estudiantes
calificaciones_clase = [
    [85, 90, 88],  # Estudiante 1
    [92, 87, 95],  # Estudiante 2
    [78, 82, 85]   # Estudiante 3
]

print("Calificaciones de la clase:")
for i, estudiante in enumerate(calificaciones_clase):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i+1}: {estudiante} - Promedio: {promedio:.1f}")

# Acceso a elementos específicos
print(f"Calificación del estudiante 2 en materia 3: {calificaciones_clase[1][2]}")

# EJEMPLO PRÁCTICO: GESTIÓN DE INVENTARIO
print("\n=== EJEMPLO PRÁCTICO: INVENTARIO DE LIBRERÍA ===")

# Lista de libros (cada libro es una lista con [título, autor, precio, stock])
inventario = [
    ["El Quijote", "Cervantes", 250, 5],
    ["Cien años de soledad", "García Márquez", 300, 3],
    ["1984", "Orwell", 280, 7],
    ["El Principito", "Saint-Exupéry", 180, 10]
]

print("📚 INVENTARIO DE LIBRERÍA")
print("-" * 60)
print(f"{'Título':<25} {'Autor':<15} {'Precio':<8} {'Stock'}")
print("-" * 60)

for libro in inventario:
    titulo, autor, precio, stock = libro  # Desempaquetado
    print(f"{titulo:<25} {autor:<15} ${precio:<7} {stock}")

# Funciones para el inventario
def buscar_libro(titulo_buscar):
    """Busca un libro por título en el inventario"""
    for libro in inventario:
        if titulo_buscar.lower() in libro[0].lower():
            return libro
    return None

def agregar_stock(titulo, cantidad):
    """Agrega stock a un libro específico"""
    libro = buscar_libro(titulo)
    if libro:
        libro[3] += cantidad
        print(f"Se agregaron {cantidad} unidades de '{libro[0]}'")
        print(f"Stock actual: {libro[3]}")
    else:
        print(f"Libro '{titulo}' no encontrado")

# Usar las funciones
print(f"\nBuscando 'Quijote': {buscar_libro('Quijote')}")
agregar_stock("1984", 3)

# COMPRENSIONES DE LISTAS (BÁSICO)
print("\n=== 7. COMPRENSIONES DE LISTAS ===")

# Lista de números pares del 1 al 20
pares = [x for x in range(1, 21) if x % 2 == 0]
print(f"Números pares del 1 al 20: {pares}")

# Lista de cuadrados
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados del 1 al 5: {cuadrados}")

# Calificaciones aprobatorias
todas_calificaciones = [65, 78, 92, 55, 88, 95, 68, 72]
aprobadas = [cal for cal in todas_calificaciones if cal >= 70]
print(f"Calificaciones aprobatorias: {aprobadas}")

# EJERCICIOS PARA EL ESTUDIANTE
print("\n=== EJERCICIOS ===")
print("1. Crea una lista con los nombres de tus 5 materias favoritas")
print("2. Implementa un sistema de playlist musical")
print("3. Crea un administrador de tareas pendientes")

# PLANTILLAS PARA EJERCICIOS
"""
# Ejercicio 1: Lista de materias favoritas
mis_materias = []
# Agrega 5 materias usando append()
# Ordena la lista alfabéticamente
# Muestra la primera y última materia

# Ejercicio 2: Playlist musical
playlist = []
# Funciones: agregar_cancion(), eliminar_cancion(), mostrar_playlist()
def agregar_cancion(cancion):
    playlist.append(cancion)
    print(f"'{cancion}' agregada a la playlist")

def eliminar_cancion(cancion):
    if cancion in playlist:
        playlist.remove(cancion)
        print(f"'{cancion}' eliminada de la playlist")
    else:
        print(f"'{cancion}' no está en la playlist")

def mostrar_playlist():
    print("🎵 PLAYLIST ACTUAL:")
    for i, cancion in enumerate(playlist, 1):
        print(f"{i}. {cancion}")

# Ejercicio 3: Administrador de tareas
tareas = []
# Implementa: agregar_tarea(), completar_tarea(), mostrar_pendientes()
"""