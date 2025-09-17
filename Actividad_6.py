# Autor: Gio Antonio Canto Gomez
# Actividad: Textos en Python
"""Descripción: presenta un menú con ejercicios de manejo de textos:
Corregir correos, Convertir notas a lista numérica, Limpiar datos de caracteres,
Verificar si el año de una fecha es bisiesto y Verificar si un apellido es palíndromo.
Las “funciones” se representan como secciones simuladas conforme al estándar.}"""

def corregir_correos():
    email = "misupergmail@gmail-com,otrocorreo@gmail-com,unacuentamas@gmail-com"
    emails_separados = email.split(",")
    emails_corregidos = []
    for correo in emails_separados:
        correo_corregido = correo.replace("-com", ".com")
        emails_corregidos.append(correo_corregido)
    print("Correos corregidos:")
    for correo in emails_corregidos:
        print(correo)

def convertir_notas():
    notas = "1, 4.3, 7.1, 4.6, 5.1, 6.6, 7.2, 8.8, 10, 9.8, 7.6"
    notas_lista = []
    for nota in notas.split(","):
        nota_float = float(nota.strip())
        notas_lista.append(nota_float)
    print("Notas convertidas:", notas_lista)

def limpiar_datos():
    datos = "aaaaaa1.2b2cde110230"
    print("Datos originales:", datos)
    datos = datos.replace("a", "").replace("b", "").replace("c", "").replace("d", "").replace("e", "")
    print("Datos limpios:", datos)

def verificar_fecha_bisiesto():
    fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
    partes = fecha.split("/")
    dia = int(partes[0])
    mes = int(partes[1])
    anyo = int(partes[2])
    if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0):
        print("El año", anyo, "es bisiesto.")
    else:
        print("El año", anyo, "no es bisiesto.")

def verificar_palindromo():
    apellido = input("Ingresa un apellido: ").lower()
    if apellido == apellido[::-1]:
        print("El apellido", apellido, "es palíndromo.")
    else:
        print("El apellido", apellido, "no es palíndromo.")


# Menú principal

while True:
    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Corregir correos electrónicos")
    print("2. Convertir notas a lista numérica")
    print("3. Limpiar datos de caracteres")
    print("4. Verificar si el año de una fecha es bisiesto")
    print("5. Verificar si un apellido es palíndromo")
    print("0. Salir")

    op = input("Elige una opción: ")
    if op == "1": corregir_correos()
    elif op == "2": convertir_notas()
    elif op == "3": limpiar_datos()
    elif op == "4": verificar_fecha_bisiesto()
    elif op == "5": verificar_palindromo()
    elif op == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
