from math import sqrt
from typing import Optional, Tuple, Union

#Controir una clase llamda raises; donde se represetnaran los valores de una ecuacion de 2do grado tendremos los 3 coeficintes como atributos
# y se llamara; A,B,C
# ahy que contrui estos 3 valres para contru un obtkro, alas oepracioens que se van a realizar , son las siguentes: 
#   A Obtener raizs imprine las 2 posibles soluciones de la manera (ObtenerRAIZ() Obtnerrazies())
#Imprimeb una unica razi que es cuando se tiene unica solcoion
# Discrimate(); devuevle el valo del discriminante obteniod por la expresion double(b2 - 4ac)
# Tieneraizes() ; devuelve un booleano "Valor logico True o false" indicando si tiene 2 soluciones, para esto el discrimita dee ser maor o igual a 0
# tieneraiz () ; devuelve un booleano "valor logico" indicadno si tiene una unica solucion; el discriminate debe ser igual a 0 mo
# caluclar () : mostrara las solcuones ue tiene nuestra ecuacion en caso de no existir solucion se debe indicar con un mensaje 

#   B


class Raises:
    def __init__(self, A: float, B: float, C: float):
        self.A = float(A)
        self.B = float(B)
        self.C = float(C)

    def Discrimate(self) -> float:
        """Devuelve el discriminante b^2 - 4ac"""
        return self.B * self.B - 4 * self.A * self.C

    def Tieneraizes(self) -> bool:
        """Según el comentario: True si el discriminante es mayor o igual a 0"""
        return self.Discrimate() >= 0

    def tieneraiz(self) -> bool:
        """True si discriminante == 0 (una única solución real)"""
        return self.Discrimate() == 0

    def ObtenerRAIZ(self) -> Optional[float]:
        """Devuelve la única raíz cuando hay discriminante == 0.
           Si no es el caso devuelve None."""
        # Si no es ecuación cuadrática tratamos el caso lineal
        if self.A == 0:
            if self.B != 0:
                return -self.C / self.B  # una raíz lineal
            return None  # sin solución o infinitas (no manejadas aquí)
        if self.tieneraiz():
            return -self.B / (2 * self.A)
        return None

    def Obtnerrazies(self) -> Optional[Tuple[float, float]]:
        """Devuelve la tupla (r1, r2) si hay soluciones reales (discriminante >= 0).
           Si no hay soluciones reales devuelve None."""
        # Caso no cuadrático (A == 0): resolver lineal si es posible
        if self.A == 0:
            if self.B != 0:
                root = -self.C / self.B
                return (root, )
            return None
        d = self.Discrimate()
        if d < 0:
            return None
        sqrt_d = sqrt(d)
        r1 = (-self.B + sqrt_d) / (2 * self.A)
        r2 = (-self.B - sqrt_d) / (2 * self.A)
        return (r1, r2)

    def caluclar(self) -> None:
        """Muestra por pantalla las soluciones según corresponda."""
        # Manejo A == 0 (no es cuadrática)
        if self.A == 0:
            if self.B == 0:
                if self.C == 0:
                    print("Infinitas soluciones (0 = 0).")
                else:
                    print("No existe solución (ecuación inconsistente).")
            else:
                root = -self.C / self.B
                print(f"Ecuación lineal. Una solución: x = {root}")
            return

        d = self.Discrimate()
        if d < 0:
            print("No existen soluciones reales.")
        elif d == 0:
            r = self.ObtenerRAIZ()
            print(f"Una única solución real: x = {r}")
        else:
            r1, r2 = self.Obtnerrazies()
            print(f"Dos soluciones reales: x1 = {r1}, x2 = {r2}")

