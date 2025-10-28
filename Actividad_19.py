class Estudiantes:
    def __init__(self, nombre, clasificacion):
        self.nombre = nombre
        self.clasificacion = clasificacion

    def mostraresultado(self):
        if self.clasificacion >= 6:
            estado = "Ha aprobado"
        else:
            estado = "Ha reprobado"
        print(f"{self.nombre} con calificación {self.clasificacion} {estado} la materia")

print("===============================================")
print("              SISTEMA DE ALUMNOS               ")
print("===============================================")
print("")

alumnos = []
i = 1
while True:
    while True:
        nombre = input(f"Escriba el nombre del alumno ({i}): ")
        if nombre.strip() == "" or nombre.isdigit():
            print("Favor de escribir un nombre válido y no un número")
        else:
            break
    while True:
        try:
            clasificacion = float(input(f"Escriba la calificación de {nombre}: "))
            break
        except ValueError:
            print("Ingrese una calificación válida (número).")
    alumno = Estudiantes(nombre, clasificacion)
    alumnos.append(alumno)
    resp1 = input("¿Desea agregar otro alumno? (si/no): ").strip().lower()
    if resp1 == "no":
        break
    print("--------------------------------------------------")
    i += 1

print("=====================================================")
print("                      RESULTADOS                    ")
print("=====================================================")
calificaciones = []
for alumno in alumnos:
    alumno.mostraresultado()
    calificaciones.append(alumno.clasificacion)
    print("--------------------------------------------------")

if calificaciones:
    media = sum(calificaciones) / len(calificaciones)
    maxima = max(calificaciones)
    minima = min(calificaciones)
    print(f"Promedio de calificaciones: {media:.2f}")
    print(f"Calificación máxima: {maxima}")
    print(f"Calificación mínima: {minima}")
else:
    print("No se ingresaron calificaciones.")
