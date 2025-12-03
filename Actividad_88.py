import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Objeto activo (focus)")

    ttk.Label(ventana, text="Escribe algo").grid(column=0, row=0, padx=10, pady=10)

    entrada = ttk.Entry(ventana, width=25)
    entrada.grid(column=0, row=1, padx=10, pady=5)

    # Objeto activo al iniciar
    entrada.focus()

    ventana.mainloop()


if __name__ == "__main__":
    main()
