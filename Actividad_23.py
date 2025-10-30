#Crear una clase estudiante:
#   Sus calificaciones son nombr, grado, grupo,especialdad, calificaicon del parcial, 1
#   Calificaion del parcial 2 y calfiacion del pacial 3
#   
#   Sus metodos seran:
#       1. Mostrar los artibutos de un obketo
#       2. Promedio para calcualr el promeido obtenido por un estudiante
#       3. CMAYOR para obtener la mayor calfiacion de los 3 parciales en que parcial fue
#       obtenida
#       Realizar lo sgieunte
#           Crear un objteo esdiante con datos estuadnte con datos fijos (Para provar metodos
#           Crear un segundo obtketo estudainte donde los valores de los artiobutos del obketo seran leidos por el teclado
#Obtener de cad auno de estatene prmoedio asi como su mayroai calfiacion ontekrda (idnaicada tmabien en que numero parical prmeiro seundo o tecereero)

#Crear una clase estudiante:
#   Sus calificaciones son nombr, grado, grupo,especialdad, calificaicon del parcial, 1
#   Calificaion del parcial 2 y calfiacion del pacial 3
#   
#   Sus metodos seran:
#       1. Mostrar los artibutos de un obketo
#       2. Promedio para calcualr el promeido obtenido por un estudiante
#       3. CMAYOR para obtener la mayor calfiacion de los 3 parciales en que parcial fue
#       obtenida
#       Realizar lo sgieunte
#           Crear un objteo esdiante con datos estuadnte con datos fijos (Para provar metodos
#           Crear un segundo obtketo estudainte donde los valores de los artiobutos del obketo seran leidos por el teclado
#Obtener de cad auno de estatene prmoedio asi como su mayroai calfiacion ontekrda (idnaicada tmabien en que numero parical prmeiro seundo o tecereero)

class Estudiante:
    def __init__(self, nombre, grado, grupo, especialidad, parcial1, parcial2, parcial3):
        self.nombre = nombre
        self.grado = grado
        self.grupo = grupo
        self.especialidad = especialidad
        self.parciales = [float(parcial1), float(parcial2), float(parcial3)]

    def mostrar_atributos(self):
        print("Nombre:", self.nombre)
        print("Grado:", self.grado)
        print("Grupo:", self.grupo)
        print("Especialidad:", self.especialidad)
        print("Calificaciones parciales:", self.parciales)

    def promedio(self):
        return sum(self.parciales) / len(self.parciales)

    def cmayor(self):
        # devuelve tupla (mayor_calificacion, numero_parcial) donde numero_parcial es 1,2 o 3
        mayor = self.parciales[0]
        indice = 1
        for i, val in enumerate(self.parciales, start=1):
            if val > mayor:
                mayor = val
                indice = i
        return mayor, indice

def leer_flotante(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Intente de nuevo (use un número).")

if __name__ == "__main__":
    # Estudiante con datos fijos (para probar métodos)
    est1 = Estudiante("Juan Pérez", 3, "A", "Matemáticas", 8.5, 7.0, 9.0)
    print("=== Estudiante 1 (datos fijos) ===")
    est1.mostrar_atributos()
    print("Promedio:", round(est1.promedio(), 2))
    mayor, parc = est1.cmayor()
    print(f"Mayor calificación: {mayor} (parcial {parc})")
    print()

    # Estudiante cuyos datos se leen por teclado
    print("=== Crear Estudiante 2 (leer por teclado) ===")
    nombre = input("Nombre: ")
    grado = input("Grado: ")
    grupo = input("Grupo: ")
    especialidad = input("Especialidad: ")
    p1 = leer_flotante("Calificación parcial 1: ")
    p2 = leer_flotante("Calificación parcial 2: ")
    p3 = leer_flotante("Calificación parcial 3: ")

    est2 = Estudiante(nombre, grado, grupo, especialidad, p1, p2, p3)
    print()
    print("=== Estudiante 2 ===")
    est2.mostrar_atributos()
    print("Promedio:", round(est2.promedio(), 2))
    mayor2, parc2 = est2.cmayor()
    print(f"Mayor calificación: {mayor2} (parcial {parc2})")