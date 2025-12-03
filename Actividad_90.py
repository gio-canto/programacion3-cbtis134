import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Lista desplegable - Combobox")

    ttk.Label(ventana, text="Selecciona un número:").grid(
        column=0, row=0, padx=10, pady=10, sticky=tk.W
    )

    numero = tk.StringVar()
    seleccionar_numero = ttk.Combobox(ventana, width=12, textvariable=numero)
    seleccionar_numero["values"] = (1, 3, 5, 7, 11)
    seleccionar_numero.grid(column=0, row=1, padx=10, pady=5)
    seleccionar_numero.current(0)

    ventana.mainloop()


if __name__ == "__main__":
    main()
