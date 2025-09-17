# Autor: Gio Antonio Canto Gomez
# Actividad: Listas en Python
"""Descripción: presenta un menú de opciones para ejecutar ejercicios básicos:
 Hola Mundo, Variables básicas, Operaciones numéricas, Interés compuesto, Ley de Ohm,
 Circunferencia y diámetro, Peso molecular, Predicción de precio de casa y Marketing CTR. 
 Las “funciones” se representan como secciones simuladas conforme al estándar."""


def evaluaciones_asignaturas():
    asignaturas = input("Inserta los nombres de las asignaturas separados por comas: ").split(",")
    evaluaciones = []
    for asignatura in asignaturas:
        num_alumnos = int(input(f"Número de alumnos en {asignatura.strip()}: "))
        puntuaciones = []
        for i in range(num_alumnos):
            nota = float(input(f"Puntuación del alumno {i+1}: "))
            puntuaciones.append(nota)
        media = sum(puntuaciones) / len(puntuaciones)
        suspensos = sum(1 for n in puntuaciones if n < 5)
        evaluaciones.append([asignatura.strip(), num_alumnos, media, suspensos])
    print("\nResultados de las evaluaciones:")
    for ev in evaluaciones:
        print(f"{ev[0]} - {ev[1]} alumnos, media {ev[2]:.2f}, suspensos {ev[3]}")

def nombres_frecuencia():
    print("Introduce nombres (escribe -1 para terminar):")
    nombres = []
    nombre = input()
    while nombre != "-1":
        nombres.extend(nombre.split(","))
        nombre = input()
    unicos, frecuencias = [], []
    for n in nombres:
        if n not in unicos:
            unicos.append(n)
            frecuencias.append(1)
        else:
            i = unicos.index(n)
            frecuencias[i] += 1
    i_max = frecuencias.index(max(frecuencias))
    print("El nombre más común es:", unicos[i_max], "con frecuencia:", frecuencias[i_max])

def tabla_multiplicar():
    num = int(input("Número para tabla de multiplicar: "))
    tabla = []
    for i in range(21):
        resultado = num * i
        tabla.append(resultado)
        print(f"{num} x {i} = {resultado}")

def lista_primos():
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    primos.sort(reverse=True)
    print("Primos de mayor a menor:", primos)

def cesta_compra():
    cesta = ["Manzanas", "Plátanos", "Naranjas", "Leche", "Pan"]
    print("Cesta original:", cesta)
    cesta.pop()
    cesta.reverse()
    print("Cesta modificada:", cesta)

def pokedex():
    nombres = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon",
               "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie"]
    ataques = [49, 62, 82, 52, 64, 84, 48, 63, 83, 30]
    hp = [45, 60, 80, 39, 58, 78, 44, 59, 79, 45]
    defensa = [49, 63, 83, 43, 58, 78, 65, 80, 100, 35]
    velocidad = [45, 60, 80, 65, 80, 100, 43, 58, 78, 45]
    at_Esp = [65, 80, 100, 60, 80, 109, 50, 65, 85, 20]
    def_Esp = [65, 80, 100, 50, 65, 85, 64, 80, 105, 20]
    pokedex = []
    for i in range(10):
        pokemon = [nombres[i], ataques[i], hp[i], defensa[i], velocidad[i], at_Esp[i], def_Esp[i]]
        pokedex.append(pokemon)
    print("Estadísticas de Pokémon:")
    for p in pokedex:
        print(p)

def planificacion_vuelos():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    planificacion = []
    for dia in dias:
        print(f"\nVuelos del día {dia}:")
        vuelos_dia = []
        while True:
            vuelo = [
                input("Hora del vuelo (HH:MM): "),
                input("Compañía aérea: "),
                input("Duración estimada: "),
                input("Tipo de avión: ")
            ]
            vuelos_dia.append(vuelo)
            continuar = input("¿Agregar otro vuelo para este día? (si/no): ")
            if continuar.lower() != "si":
                break
        planificacion.append(vuelos_dia)
    print("\nPlanificación completa:")
    for i, vuelos in enumerate(planificacion):
        print(dias[i])
        for v in vuelos:
            print("Hora:", v[0], "Compañía:", v[1], "Duración:", v[2], "Avión:", v[3])
            print("--------------------")

# Menú principal

while True:
    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Evaluaciones por asignatura")
    print("2. Frecuencia de nombres")
    print("3. Tabla de multiplicar")
    print("4. Lista de primos ordenados")
    print("5. Cesta de la compra")
    print("6. Pokedex")
    print("7. Planificación de vuelos")
    print("0. Salir")

    op = input("Elige una opción: ")
    if op == "1": evaluaciones_asignaturas()
    elif op == "2": nombres_frecuencia()
    elif op == "3": tabla_multiplicar()
    elif op == "4": lista_primos()
    elif op == "5": cesta_compra()
    elif op == "6": pokedex()
    elif op == "7": planificacion_vuelos()
    elif op == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
