"""
Actividad 3.2: Juego Adivina el Número
Objetivo: Aplicar estructuras de control en un proyecto divertido
"""

import random

print("🎯 BIENVENIDO AL JUEGO: ADIVINA EL NÚMERO 🎯")
print("="*50)

# VERSIÓN BÁSICA DEL JUEGO
def juego_basico():
    """Versión simple del juego para aprender conceptos básicos"""
    print("\n=== VERSIÓN BÁSICA ===")
    
    # La computadora elige un número entre 1 y 10
    numero_secreto = random.randint(1, 10)
    print("He pensado en un número entre 1 y 10")
    print("¡Trata de adivinarlo!")
    
    # El jugador tiene 3 intentos
    intentos = 3
    
    for intento in range(1, intentos + 1):
        print(f"\nIntento {intento} de {intentos}")
        
        # Capturar la adivinanza del jugador
        try:
            adivinanza = int(input("Tu número: "))
        except ValueError:
            print("Por favor, ingresa un número válido")
            continue
        
        # Verificar si adivinó
        if adivinanza == numero_secreto:
            print(f"🎉 ¡FELICITACIONES! Adivinaste en {intento} intentos")
            return True
        elif adivinanza < numero_secreto:
            print("📈 El número que busquas es MAYOR")
        else:
            print("📉 El número que buscas es MENOR")
    
    print(f"\n😔 Se acabaron los intentos. El número era {numero_secreto}")
    return False

# VERSIÓN AVANZADA DEL JUEGO
def juego_avanzado():
    """Versión más compleja con más características"""
    print("\n=== VERSIÓN AVANZADA ===")
    
    # Configuración del juego
    print("Elige la dificultad:")
    print("1. Fácil (1-20, 6 intentos)")
    print("2. Medio (1-50, 5 intentos)")
    print("3. Difícil (1-100, 4 intentos)")
    
    while True:
        try:
            dificultad = int(input("Dificultad (1-3): "))
            if dificultad in [1, 2, 3]:
                break
            else:
                print("Elige 1, 2 o 3")
        except ValueError:
            print("Ingresa un número válido")
    
    # Configurar según dificultad
    if dificultad == 1:
        max_numero = 20
        max_intentos = 6
        nivel = "FÁCIL"
    elif dificultad == 2:
        max_numero = 50
        max_intentos = 5
        nivel = "MEDIO"
    else:
        max_numero = 100
        max_intentos = 4
        nivel = "DIFÍCIL"
    
    # Generar número secreto
    numero_secreto = random.randint(1, max_numero)
    
    print(f"\n🎯 Nivel {nivel}")
    print(f"Adivina el número entre 1 y {max_numero}")
    print(f"Tienes {max_intentos} intentos")
    
    # Jugar
    intentos_usados = 0
    numeros_probados = []
    
    while intentos_usados < max_intentos:
        intentos_restantes = max_intentos - intentos_usados
        print(f"\nIntentos restantes: {intentos_restantes}")
        
        if numeros_probados:
            print(f"Números ya probados: {sorted(numeros_probados)}")
        
        # Capturar adivinanza
        try:
            adivinanza = int(input(f"Tu número (1-{max_numero}): "))
        except ValueError:
            print("Ingresa un número válido")
            continue
        
        # Validar rango
        if adivinanza < 1 or adivinanza > max_numero:
            print(f"El número debe estar entre 1 y {max_numero}")
            continue
        
        # Verificar si ya lo probó
        if adivinanza in numeros_probados:
            print("Ya probaste ese número")
            continue
        
        # Contar intento y agregar a la lista
        intentos_usados += 1
        numeros_probados.append(adivinanza)
        
        # Verificar si adivinó
        if adivinanza == numero_secreto:
            print(f"🎉 ¡EXCELENTE! Adivinaste en {intentos_usados} intentos")
            
            # Evaluar performance
            if intentos_usados == 1:
                print("🏆 ¡INCREÍBLE! Lo lograste en el primer intento")
            elif intentos_usados <= max_intentos // 2:
                print("⭐ ¡MUY BIEN! Excelente estrategia")
            else:
                print("👍 ¡BIEN HECHO! Lo lograste")
            
            return True
        
        # Dar pista
        diferencia = abs(adivinanza - numero_secreto)
        
        if diferencia <= 2:
            print("🔥 ¡MUY CALIENTE! Estás muy cerca")
        elif diferencia <= 5:
            print("🌡️ Caliente")
        elif diferencia <= 10:
            print("🌤️ Tibio")
        else:
            print("❄️ Frío")
        
        # Indicar dirección
        if adivinanza < numero_secreto:
            print("📈 El número es MAYOR")
        else:
            print("📉 El número es MENOR")
    
    print(f"\n😔 ¡Juego terminado! El número era {numero_secreto}")
    return False

# SISTEMA DE PUNTUACIÓN
def jugar_con_puntos():
    """Versión con sistema de puntuación"""
    print("\n=== JUEGO CON PUNTUACIÓN ===")
    
    puntos_totales = 0
    juegos_jugados = 0
    juegos_ganados = 0
    
    while True:
        print(f"\n--- JUEGO #{juegos_jugados + 1} ---")
        print(f"Puntos totales: {puntos_totales}")
        
        # Jugar una ronda
        if juego_avanzado():
            juegos_ganados += 1
            # Puntos según intentos (menos intentos = más puntos)
            puntos_ronda = 10  # Puntos base por ganar
            puntos_totales += puntos_ronda
            print(f"¡Ganaste {puntos_ronda} puntos!")
        
        juegos_jugados += 1
        
        # Mostrar estadísticas
        if juegos_jugados > 0:
            porcentaje_victorias = (juegos_ganados / juegos_jugados) * 100
            print(f"\nEstadísticas:")
            print(f"Juegos jugados: {juegos_jugados}")
            print(f"Juegos ganados: {juegos_ganados}")
            print(f"Porcentaje de victorias: {porcentaje_victorias:.1f}%")
            print(f"Puntos totales: {puntos_totales}")
        
        # Preguntar si quiere jugar otra vez
        otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if otra_vez != 's':
            break
    
    print(f"\n🏆 JUEGO TERMINADO 🏆")
    print(f"Puntuación final: {puntos_totales} puntos")
    print("¡Gracias por jugar!")

# MENÚ PRINCIPAL
def menu_principal():
    """Menú para elegir qué versión del juego jugar"""
    while True:
        print("\n" + "="*50)
        print("🎯 MENÚ PRINCIPAL")
        print("="*50)
        print("1. Juego Básico (Aprender conceptos)")
        print("2. Juego Avanzado (Más desafío)")
        print("3. Juego con Puntuación (Competitivo)")
        print("4. Salir")
        
        try:
            opcion = int(input("\nElige una opción (1-4): "))
        except ValueError:
            print("Ingresa un número válido")
            continue
        
        if opcion == 1:
            juego_basico()
        elif opcion == 2:
            juego_avanzado()
        elif opcion == 3:
            jugar_con_puntos()
        elif opcion == 4:
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción no válida. Elige 1, 2, 3 o 4")

# EJECUTAR EL JUEGO
if __name__ == "__main__":
    menu_principal()

# EJERCICIOS PARA EL ESTUDIANTE
"""
EJERCICIOS DE EXTENSIÓN:

1. Agrega un modo de dos jugadores donde se turnen para adivinar
2. Implementa un sistema de niveles que desbloquee rangos más grandes
3. Crea una versión donde el jugador piense el número y la computadora adivine
4. Agrega un temporizador para cada intento
5. Implementa diferentes tipos de pistas (par/impar, múltiplo de X, etc.)

CONCEPTOS APLICADOS:
- Estructuras condicionales (if, elif, else)
- Bucles (for, while)
- Manejo de excepciones (try, except)
- Funciones
- Listas y manipulación de datos
- Validación de entrada
- Lógica de juegos
"""