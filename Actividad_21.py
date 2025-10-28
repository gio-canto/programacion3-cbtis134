from datetime import datetime 
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class Persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = int(edad)
        sexo = sexo or "h"
        self.sexo = sexo.lower() if sexo.lower() in ("h", "m") else "h"
        self.peso = float(peso)
        self.altura = float(altura)  # en cm

    def calcular_imc(self):
        altura_m = self.altura / 100
        return self.peso / (altura_m * altura_m)

    def categoria_imc(self, imc):
        if imc < 18.5:
            return "bajo peso"
        elif imc < 25:
            return "peso ideal"
        elif imc < 30:
            return "sobrepeso"
        else:
            return "obesidad"

    def es_mayor(self):
        return self.edad >= 18

    def mostrar(self):
        imc = self.calcular_imc()
        categoria = self.categoria_imc(imc)
        print("==============================")
        print("Nombre:", self.nombre)
        print("Edad  :", self.edad, "años -", "mayor" if self.es_mayor() else "menor", "de edad")
        print("Sexo  :", "Hombre" if self.sexo == "h" else "Mujer")
        print("Peso  :", f"{self.peso:.2f} kg")
        print("Altura:", f"{self.altura:.1f} cm")
        print("IMC   :", f"{imc:.2f}", "->", categoria)
        print("==============================")


def main():
    ahora = datetime.now()
    print("=== CALCULADORA IMC (10 PERSONAS) ===")
    print("Fecha y hora:", ahora.strftime("%Y-%m-%d %H:%M:%S"))
    print()

    personas = []
    for i in range(10):
        print(f"--- Datos persona {i+1} ---")
        nombre = input("Nombre: ") or f"Persona {i+1}"
        edad = int(input("Edad (años): ") or 18)
        sexo = input("Sexo (h/m): ") or "h"
        peso = float(input("Peso (kg): ") or 70)
        altura = float(input("Altura (cm): ") or 170)
        personas.append(Persona(nombre, edad, sexo, peso, altura))
        print()

    limpiar_pantalla()
    print("\nResultados:")
    for p in personas:
        p.mostrar()

if __name__ == "__main__":
    main()
