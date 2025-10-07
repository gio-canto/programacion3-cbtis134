"""
Clase CuentaBancaria

Esta clase representa una cuenta bancaria con los siguientes atributos:
- numero_cuenta: Número de la cuenta bancaria.
- id_cliente: Identificador único del cliente.
- saldo: Saldo actual de la cuenta.

Métodos:
1. ingresar(cantidad): Permite hacer un depósito de una cierta cantidad en la cuenta.
2. retirar(cantidad): Permite retirar dinero de la cuenta solo si el saldo es suficiente.
3. ver_saldo(): Permite visualizar el saldo actual de la cuenta.

Se deben crear tres objetos de esta clase y utilizar los métodos de ingresar, retirar y ver saldo en cada uno de ellos.

#Crear una claese/cuenta bancaria con atributos para el nuemro de cuenta, la ID del cliente y es saldo actual, define en la clase los siguentes metodos,
1 Ingresar, permite hacer un deposito de una ceirta canitdad, 
2   retirar, permite sacar dinero de la cuenta solo si el saldo es suficiente-
3 metodo para visualziar el saldo actual, se deben crear 3 objetos de esta clase donde se utilze  los metodos de ingresas, retriar y ver saldo"""

import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class CuentaBancaria:
    def __init__(self, numero_cuenta, id_cliente, saldo):
        self.numero_cuenta = numero_cuenta
        self.id_cliente = id_cliente
        self.saldo = saldo

    def opcionesCajero(self):
        while True:
            limpiar_pantalla()
            print("================================")
            print("Bienvenido {} a su cuenta bancaria {}".format(self.id_cliente, self.numero_cuenta))
            print("================================")
            print("\nSeleccione una opción:\n")
            print("(1) Retiro")
            print("(2) Depósito")
            print("(3) Consulta de saldo")
            print("(4) Salir")

            opcion = input("> ").strip()
            if opcion not in {"1", "2", "3", "4"}:
                print("\nDebe ingresar una opción válida.")
                time.sleep(1.5)
                continue
            if opcion == "4":
                limpiar_pantalla()
                self.salida()
                break
            elif opcion == "1":
                self.retirar()
            elif opcion == "2":
                self.deposito()
            elif opcion == "3":
                self.ver_saldo()

    def deposito(self):
        while True:
            limpiar_pantalla()
            print("================================")
            print("Depósito")
            print("================================")
            cant_str = input("Ingrese la cantidad a depositar: ").strip()
            try:
                deposito = float(cant_str)
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")
                time.sleep(1.5)
                continue

            if deposito <= 0:
                print("Cantidad inválida. Intente de nuevo.")
                time.sleep(1.5)
                continue

            print(f"¿Está seguro que desea depositar {deposito}?")
            confirmacion = input("Escriba 'si' para confirmar o 'no' para cancelar: ").strip().lower()
            if confirmacion == 'si':
                limpiar_pantalla()
                print("Su solicitud está siendo procesada, por favor espere...")
                time.sleep(1.2)
                self.saldo += deposito
                print(f"Depósito de {deposito} realizado al usuario: {self.id_cliente}. Nuevo saldo: {self.saldo}")
                print("Gracias por su preferencia. :D")
                time.sleep(2)
            else:
                print("Depósito cancelado.")
                time.sleep(1.2)
            break

    def retirar(self):
        while True:
            limpiar_pantalla()
            print("================================")
            print("Retiro")
            print("================================")
            cant_str = input("Ingrese la cantidad a retirar: ").strip()
            try:
                retiro = float(cant_str)
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")
                time.sleep(1.5)
                continue

            if retiro <= 0:
                print("Cantidad inválida. Intente de nuevo.")
                time.sleep(1.5)
                continue

            if retiro > self.saldo:
                print("Saldo insuficiente. Intente de nuevo.")
                time.sleep(1.5)
                continue

            print(f"¿Está seguro que desea retirar {retiro}?")
            confirmacion = input("Escriba 'si' para confirmar o 'no' para cancelar: ").strip().lower()
            if confirmacion == 'si':
                limpiar_pantalla()
                print("Su solicitud está siendo procesada, por favor espere...")
                time.sleep(5)
                self.saldo -= retiro
                print(f"Retiro de {retiro} realizado al usuario: {self.id_cliente}. Nuevo saldo: {self.saldo}")
                print("Gracias por su preferencia. :D")
                time.sleep(2)
            else:
                print("Retiro cancelado.")
                time.sleep(1.2)
            break

    def ver_saldo(self):
        limpiar_pantalla()
        print("================================")
        print("Saldo Actual")
        print("================================")
        print(f"El saldo de la cuenta {self.numero_cuenta} del cliente {self.id_cliente} es: {self.saldo}")
        time.sleep(2.5)

    def salida(self):
        print("===========================")
        print("Muchas gracias por usar los servicios de:")
        print("Banco Chafa, S.A., Institución de Banca Múltiple.")
        print("===========================")

# --- Programa principal ---

print("Bienvenido a Banco Chafa, S.A., Institución de Banca Múltiple.")
print('Donde tu dinero está "seguro" con nosotros.')
usuario_1 = input("Ingrese su usuario: ").strip()

if usuario_1 == "I2099":
    cuenta = CuentaBancaria(989293892332, 2099, 1_000_000.00)
    cuenta.opcionesCajero()
elif usuario_1 == "I3894":
    cuenta = CuentaBancaria(989293895633, 3894, 923.23)
    cuenta.opcionesCajero()
elif usuario_1 == "I0001":
    cuenta = CuentaBancaria(989293892312, 1, 932.34)
    cuenta.opcionesCajero()
else:
    print("Su usuario no existe en nuestra base.")
