"""
PROYECTO INTEGRADOR: Sistema de Gestión Escolar CBTIS
Objetivo: Aplicar todos los conceptos aprendidos en un proyecto práctico
Autor: Estudiante de 3er Semestre CBTIS
"""

import random
from datetime import datetime

print("🎓 SISTEMA DE GESTIÓN ESCOLAR CBTIS 🎓")
print("="*50)

# DATOS GLOBALES
estudiantes = []
materias = ["Matemáticas", "Física", "Química", "Inglés", "Historia", "Programación"]
calificaciones_db = {}

# FUNCIONES DE UTILIDAD
def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("📋 MENÚ PRINCIPAL")
    print("="*50)
    print("1. 👥 Gestión de Estudiantes")
    print("2. 📊 Gestión de Calificaciones")
    print("3. 📈 Reportes y Estadísticas")
    print("4. 🎯 Mini-Juegos Educativos")
    print("5. 💾 Guardar y Cargar Datos")
    print("0. 🚪 Salir")
    print("="*50)

def limpiar_pantalla():
    """Simula limpiar la pantalla"""
    print("\n" * 3)

# GESTIÓN DE ESTUDIANTES
def agregar_estudiante():
    """Agrega un nuevo estudiante al sistema"""
    print("\n➕ AGREGAR ESTUDIANTE")
    print("-" * 30)
    
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    
    while True:
        try:
            edad = int(input("Edad: "))
            if 15 <= edad <= 20:
                break
            else:
                print("La edad debe estar entre 15 y 20 años")
        except ValueError:
            print("Ingresa una edad válida")
    
    semestre = input("Semestre (1-6): ").strip()
    
    # Crear ID único
    estudiante_id = len(estudiantes) + 1
    
    estudiante = {
        'id': estudiante_id,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'semestre': semestre,
        'fecha_registro': datetime.now().strftime("%d/%m/%Y")
    }
    
    estudiantes.append(estudiante)
    calificaciones_db[estudiante_id] = {}
    
    print(f"✅ Estudiante {nombre} {apellido} agregado exitosamente!")
    print(f"ID asignado: {estudiante_id}")

def mostrar_estudiantes():
    """Muestra todos los estudiantes registrados"""
    if not estudiantes:
        print("❌ No hay estudiantes registrados")
        return
    
    print(f"\n👥 ESTUDIANTES REGISTRADOS ({len(estudiantes)})")
    print("-" * 80)
    print(f"{'ID':<4} {'Nombre':<15} {'Apellido':<15} {'Edad':<5} {'Semestre':<9} {'Registro'}")
    print("-" * 80)
    
    for estudiante in estudiantes:
        print(f"{estudiante['id']:<4} {estudiante['nombre']:<15} "
              f"{estudiante['apellido']:<15} {estudiante['edad']:<5} "
              f"{estudiante['semestre']:<9} {estudiante['fecha_registro']}")

def buscar_estudiante(id_buscar=None):
    """Busca un estudiante por ID"""
    if id_buscar is None:
        try:
            id_buscar = int(input("ID del estudiante: "))
        except ValueError:
            print("ID debe ser un número")
            return None
    
    for estudiante in estudiantes:
        if estudiante['id'] == id_buscar:
            return estudiante
    
    print(f"❌ No se encontró estudiante con ID {id_buscar}")
    return None

# GESTIÓN DE CALIFICACIONES
def agregar_calificacion():
    """Agrega una calificación a un estudiante"""
    if not estudiantes:
        print("❌ Primero debes registrar estudiantes")
        return
    
    print("\n📝 AGREGAR CALIFICACIÓN")
    print("-" * 30)
    
    estudiante = buscar_estudiante()
    if not estudiante:
        return
    
    print(f"\nEstudiante: {estudiante['nombre']} {estudiante['apellido']}")
    print("Materias disponibles:")
    for i, materia in enumerate(materias, 1):
        print(f"{i}. {materia}")
    
    try:
        opcion_materia = int(input("Selecciona materia (1-6): ")) - 1
        if opcion_materia < 0 or opcion_materia >= len(materias):
            print("Opción inválida")
            return
        
        materia_seleccionada = materias[opcion_materia]
        
        calificacion = float(input("Calificación (0-100): "))
        if calificacion < 0 or calificacion > 100:
            print("La calificación debe estar entre 0 y 100")
            return
        
        # Agregar calificación
        estudiante_id = estudiante['id']
        if materia_seleccionada not in calificaciones_db[estudiante_id]:
            calificaciones_db[estudiante_id][materia_seleccionada] = []
        
        calificaciones_db[estudiante_id][materia_seleccionada].append(calificacion)
        
        print(f"✅ Calificación {calificacion} agregada en {materia_seleccionada}")
        
    except ValueError:
        print("Valores inválidos")

def mostrar_calificaciones_estudiante():
    """Muestra las calificaciones de un estudiante específico"""
    if not estudiantes:
        print("❌ No hay estudiantes registrados")
        return
    
    estudiante = buscar_estudiante()
    if not estudiante:
        return
    
    estudiante_id = estudiante['id']
    print(f"\n📊 CALIFICACIONES DE {estudiante['nombre'].upper()} {estudiante['apellido'].upper()}")
    print("-" * 60)
    
    if estudiante_id not in calificaciones_db or not calificaciones_db[estudiante_id]:
        print("❌ No hay calificaciones registradas")
        return
    
    total_calificaciones = 0
    suma_promedios = 0
    materias_con_calificaciones = 0
    
    for materia, califs in calificaciones_db[estudiante_id].items():
        if califs:
            promedio = sum(califs) / len(califs)
            suma_promedios += promedio
            materias_con_calificaciones += 1
            total_calificaciones += len(califs)
            
            status = "✅ APROBADA" if promedio >= 70 else "❌ REPROBADA"
            print(f"{materia:<15}: {califs} → Promedio: {promedio:.1f} {status}")
    
    if materias_con_calificaciones > 0:
        promedio_general = suma_promedios / materias_con_calificaciones
        print("-" * 60)
        print(f"PROMEDIO GENERAL: {promedio_general:.2f}")
        print(f"MATERIAS CURSADAS: {materias_con_calificaciones}")
        print(f"CALIFICACIONES TOTALES: {total_calificaciones}")

# REPORTES Y ESTADÍSTICAS
def generar_reporte_grupal():
    """Genera estadísticas del grupo"""
    if not estudiantes:
        print("❌ No hay estudiantes registrados")
        return
    
    print(f"\n📈 REPORTE GRUPAL")
    print("=" * 50)
    
    # Estadísticas generales
    total_estudiantes = len(estudiantes)
    edades = [est['edad'] for est in estudiantes]
    edad_promedio = sum(edades) / len(edades)
    
    print(f"Total de estudiantes: {total_estudiantes}")
    print(f"Edad promedio: {edad_promedio:.1f} años")
    print(f"Edad mínima: {min(edades)} años")
    print(f"Edad máxima: {max(edades)} años")
    
    # Distribución por semestre
    semestres = {}
    for estudiante in estudiantes:
        sem = estudiante['semestre']
        semestres[sem] = semestres.get(sem, 0) + 1
    
    print(f"\n📚 DISTRIBUCIÓN POR SEMESTRE:")
    for semestre, cantidad in sorted(semestres.items()):
        print(f"Semestre {semestre}: {cantidad} estudiantes")
    
    # Estadísticas de calificaciones
    todas_calificaciones = []
    estudiantes_con_calificaciones = 0
    
    for estudiante_id, materias_califs in calificaciones_db.items():
        if materias_califs:
            estudiantes_con_calificaciones += 1
            for materia, califs in materias_califs.items():
                todas_calificaciones.extend(califs)
    
    if todas_calificaciones:
        print(f"\n📊 ESTADÍSTICAS DE CALIFICACIONES:")
        print(f"Estudiantes con calificaciones: {estudiantes_con_calificaciones}")
        print(f"Total de calificaciones: {len(todas_calificaciones)}")
        print(f"Promedio general del grupo: {sum(todas_calificaciones)/len(todas_calificaciones):.2f}")
        print(f"Calificación más alta: {max(todas_calificaciones)}")
        print(f"Calificación más baja: {min(todas_calificaciones)}")
        
        # Distribución de calificaciones
        excelentes = len([c for c in todas_calificaciones if c >= 90])
        buenas = len([c for c in todas_calificaciones if 80 <= c < 90])
        regulares = len([c for c in todas_calificaciones if 70 <= c < 80])
        reprobadas = len([c for c in todas_calificaciones if c < 70])
        
        print(f"\n🏆 DISTRIBUCIÓN DE CALIFICACIONES:")
        print(f"Excelentes (90-100): {excelentes}")
        print(f"Buenas (80-89): {buenas}")
        print(f"Regulares (70-79): {regulares}")
        print(f"Reprobadas (<70): {reprobadas}")

# MINI-JUEGOS EDUCATIVOS
def juego_matematicas():
    """Mini-juego de matemáticas para estudiantes"""
    print(f"\n🎯 JUEGO DE MATEMÁTICAS")
    print("-" * 30)
    print("Resuelve 5 operaciones matemáticas")
    
    puntaje = 0
    total_preguntas = 5
    
    for i in range(1, total_preguntas + 1):
        # Generar operación aleatoria
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        operacion = random.choice(['+', '-', '*'])
        
        if operacion == '+':
            respuesta_correcta = a + b
        elif operacion == '-':
            respuesta_correcta = a - b
        else:  # multiplicación
            respuesta_correcta = a * b
        
        print(f"\nPregunta {i}: {a} {operacion} {b} = ?")
        
        try:
            respuesta_usuario = int(input("Tu respuesta: "))
            if respuesta_usuario == respuesta_correcta:
                print("✅ ¡Correcto!")
                puntaje += 1
            else:
                print(f"❌ Incorrecto. La respuesta era {respuesta_correcta}")
        except ValueError:
            print(f"❌ Respuesta inválida. La respuesta era {respuesta_correcta}")
    
    print(f"\n🏆 RESULTADO FINAL")
    print(f"Puntaje: {puntaje}/{total_preguntas}")
    porcentaje = (puntaje / total_preguntas) * 100
    print(f"Porcentaje: {porcentaje:.1f}%")
    
    if porcentaje >= 80:
        print("🌟 ¡Excelente trabajo!")
    elif porcentaje >= 60:
        print("👍 ¡Buen trabajo!")
    else:
        print("📚 ¡Sigue practicando!")

def quiz_conocimientos():
    """Quiz de conocimientos generales"""
    print(f"\n🧠 QUIZ DE CONOCIMIENTOS")
    print("-" * 30)
    
    preguntas = [
        {
            "pregunta": "¿Cuál es la capital de México?",
            "opciones": ["a) Guadalajara", "b) Ciudad de México", "c) Monterrey"],
            "correcta": "b"
        },
        {
            "pregunta": "¿En qué año se inventó Python?",
            "opciones": ["a) 1989", "b) 1991", "c) 1995"],
            "correcta": "b"
        },
        {
            "pregunta": "¿Cuál es la fórmula del agua?",
            "opciones": ["a) H2O", "b) CO2", "c) NaCl"],
            "correcta": "a"
        }
    ]
    
    puntaje = 0
    
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)
        
        respuesta = input("Tu respuesta (a/b/c): ").lower().strip()
        
        if respuesta == pregunta['correcta']:
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta era {pregunta['correcta']}")
    
    print(f"\n🏆 Puntaje final: {puntaje}/{len(preguntas)}")

# SIMULACIÓN DE DATOS DE EJEMPLO
def cargar_datos_ejemplo():
    """Carga datos de ejemplo para probar el sistema"""
    global estudiantes, calificaciones_db
    
    # Estudiantes de ejemplo
    estudiantes_ejemplo = [
        {"nombre": "María", "apellido": "González", "edad": 17, "semestre": "3"},
        {"nombre": "Juan", "apellido": "Pérez", "edad": 16, "semestre": "3"},
        {"nombre": "Ana", "apellido": "López", "edad": 18, "semestre": "4"},
        {"nombre": "Carlos", "apellido": "Rodríguez", "edad": 17, "semestre": "3"},
        {"nombre": "Laura", "apellido": "Martínez", "edad": 16, "semestre": "2"}
    ]
    
    for i, datos in enumerate(estudiantes_ejemplo, 1):
        estudiante = {
            'id': i,
            'nombre': datos['nombre'],
            'apellido': datos['apellido'],
            'edad': datos['edad'],
            'semestre': datos['semestre'],
            'fecha_registro': "15/09/2024"
        }
        estudiantes.append(estudiante)
        
        # Agregar calificaciones aleatorias
        calificaciones_db[i] = {}
        for materia in random.sample(materias, random.randint(2, 4)):
            num_calificaciones = random.randint(1, 3)
            calificaciones_db[i][materia] = [
                random.randint(60, 100) for _ in range(num_calificaciones)
            ]
    
    print("✅ Datos de ejemplo cargados exitosamente!")
    print(f"Se cargaron {len(estudiantes)} estudiantes con calificaciones aleatorias")

# FUNCIÓN PRINCIPAL
def main():
    """Función principal del sistema"""
    print("Bienvenido al Sistema de Gestión Escolar CBTIS")
    print("Desarrollado por estudiantes de 3er semestre")
    
    # Cargar datos de ejemplo automáticamente
    cargar_datos_ejemplo()
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                print("\n👥 GESTIÓN DE ESTUDIANTES")
                print("1. Agregar estudiante")
                print("2. Mostrar estudiantes")
                print("3. Buscar estudiante")
                
                sub_opcion = input("Opción: ")
                if sub_opcion == "1":
                    agregar_estudiante()
                elif sub_opcion == "2":
                    mostrar_estudiantes()
                elif sub_opcion == "3":
                    buscar_estudiante()
                    
            elif opcion == "2":
                print("\n📊 GESTIÓN DE CALIFICACIONES")
                print("1. Agregar calificación")
                print("2. Ver calificaciones de estudiante")
                
                sub_opcion = input("Opción: ")
                if sub_opcion == "1":
                    agregar_calificacion()
                elif sub_opcion == "2":
                    mostrar_calificaciones_estudiante()
                    
            elif opcion == "3":
                generar_reporte_grupal()
                
            elif opcion == "4":
                print("\n🎯 MINI-JUEGOS EDUCATIVOS")
                print("1. Juego de Matemáticas")
                print("2. Quiz de Conocimientos")
                
                sub_opcion = input("Opción: ")
                if sub_opcion == "1":
                    juego_matematicas()
                elif sub_opcion == "2":
                    quiz_conocimientos()
                    
            elif opcion == "5":
                print("\n💾 GESTIÓN DE DATOS")
                print("1. Cargar datos de ejemplo")
                print("2. Mostrar estadísticas actuales")
                
                sub_opcion = input("Opción: ")
                if sub_opcion == "1":
                    cargar_datos_ejemplo()
                elif sub_opcion == "2":
                    print(f"Estudiantes registrados: {len(estudiantes)}")
                    print(f"Registros de calificaciones: {len(calificaciones_db)}")
                    
            elif opcion == "0":
                print("\n👋 ¡Gracias por usar el Sistema de Gestión Escolar CBTIS!")
                print("¡Que tengas un excelente día!")
                break
                
            else:
                print("❌ Opción no válida")
                
        except KeyboardInterrupt:
            print("\n\n👋 Sistema cerrado por el usuario")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\nPresiona Enter para continuar...")

# EJECUTAR EL PROGRAMA
if __name__ == "__main__":
    main()