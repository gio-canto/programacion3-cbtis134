import tkinter as tk
from tkinter import messagebox


def main():
    ventana = tk.Tk()
    ventana.title("Calculadora Simple")
    ventana.geometry("300x200")

    resultado = tk.StringVar(value="Resultado: ")

    def calcular():
        """Calcula la suma de dos números ingresados."""
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            resultado.set(f"Resultado: {num1 + num2}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa números válidos.")

    tk.Label(ventana, text="Número 1:").pack()
    entry1 = tk.Entry(ventana)
    entry1.pack()

    tk.Label(ventana, text="Número 2:").pack()
    entry2 = tk.Entry(ventana)
    entry2.pack()

    tk.Button(ventana, text="Sumar", command=calcular).pack(pady=10)
    tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack()

    ventana.mainloop()


if __name__ == "__main__":
    main()
