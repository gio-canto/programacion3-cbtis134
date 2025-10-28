"""Clase Libro que almacena la información bibliográfica (estilo BibTeX) de un libro.

Atributos:
    titulo (str): Título del libro.
    edicion (str|int): Edición del libro.
    autor (str|list): Autor o lista de autores.
    isbn (str): Código ISBN.
    editorial (str): Nombre de la editorial.
    fecha_edicion (str|date): Fecha de edición/publicación.
    num_paginas (int): Número de páginas.

Métodos:
    leer_datos(...): Leer o recibir los datos del libro (por ejemplo desde entrada o parámetros).
    mostrar_datos(): Devolver o imprimir la información recopilada en un formato legible.

La clase debe encargarse de validar y formatear los campos básicos (p. ej. ISBN, fecha) cuando sea necesario.
"""
"""
Clase Libro que almacena la información bibliográfica (estilo BibTeX) de un libro.

Atributos:
    titulo (str)
    edicion (str|int)
    autor (str|list[str])
    isbn (str)
    editorial (str)
    fecha_edicion (str|date)
    num_paginas (int|None)
    url (str)
    nota (str)

Métodos:
    leer_datos(): Solicita datos por entrada estándar con validación (incluye ISBN).
    mostrar_datos(): Imprime la ficha del libro.
"""

import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class Libro:
    def __init__(self):
        self.titulo = ""
        self.edicion = ""
        self.autor = ""
        self.isbn = "N/A"
        self.editorial = ""
        self.fecha_edicion = ""
        self.direccion_editorial = ""
        self.num_paginas = None
        self.url = ""
        self.nota = ""

    @staticmethod
    def _isbn_valido(txt: str) -> bool:
        """Valida ISBN-10/13. Acepta guiones/espacios. 'N/A' permitido externamente."""
        s = txt.replace('-', '').replace(' ', '')
        if len(s) == 10 and all(c.isdigit() for c in s[:9]) and (s[-1].isdigit() or s[-1] in 'Xx'):
            total = sum((10 - i) * (10 if ch in 'Xx' else int(ch)) for i, ch in enumerate(s))
            return total % 11 == 0
        if len(s) == 13 and s.isdigit():
            total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(s[:12]))
            return (10 - total % 10) % 10 == int(s[12])
        return False

    def leer_datos(self):
        limpiar_pantalla()
        sep = "=*" * 20
        print(sep); print("Ingrese los datos del libro"); print(sep)

        self.titulo = input("Título del libro: ").strip()
        self.edicion = input("Edición del libro: ").strip()

        a = input("Autor(es) (separe con coma si son varios): ").strip()
        self.autor = [x.strip() for x in a.split(",")] if "," in a else a

        # ISBN con validación
        while True:
            t = input("Código ISBN (o N/A): ").strip()
            if not t or t.upper() in {"N/A", "NA"}:
                self.isbn = "N/A"
                break
            if self._isbn_valido(t):
                self.isbn = t
                print(f"ISBN válido: {t}")
                break
            print("ISBN inválido. Intente de nuevo.")

        self.editorial = input("Nombre de la editorial: ").strip()
        self.fecha_edicion = input("Fecha de edición/publicación: ").strip()
        self.direccion_editorial = input("Dirección de la editorial: ").strip()

        p = input("Número de páginas (entero o vacío): ").strip()
        self.num_paginas = int(p) if p.isdigit() else None

        self.url = input("URL del libro (si aplica): ").strip()
        self.nota = input("Notas adicionales (si aplica): ").strip()

    def mostrar_datos(self):
        sep = "=*" * 20
        print(sep); print("Datos del libro ingresados"); print(sep)
        print(f"Título: {self.titulo or 'N/A'}")
        print(f"Edición: {self.edicion or 'N/A'}")
        if isinstance(self.autor, list):
            print(f"Autor(es): {', '.join(self.autor) if self.autor else 'N/A'}")
        else:
            print(f"Autor: {self.autor or 'N/A'}")
        print(f"ISBN: {self.isbn or 'N/A'}")
        print(f"Editorial: {self.editorial or 'N/A'}")
        print(f"Fecha de edición/publicación: {self.fecha_edicion or 'N/A'}")
        print(f"Dirección de la editorial: {self.direccion_editorial or 'N/A'}")
        print(f"Número de páginas: {self.num_paginas if self.num_paginas is not None else 'N/A'}")
        print(f"URL: {self.url or 'N/A'}")
        print(f"Notas adicionales: {self.nota or 'N/A'}")
        print(sep)

if __name__ == "__main__":
    print("Librería del Hipnos")
    try:
        cantidad = int(input("¿Cuántos libros desea ingresar? "))
    except ValueError:
        cantidad = 1

    libros = []
    for _ in range(max(1, cantidad)):
        libro = Libro()
        libro.leer_datos()
        libros.append(libro)

    limpiar_pantalla()
    for libro in libros:
        libro.mostrar_datos()
