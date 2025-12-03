import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("LabelFrame - Cajas de etiquetas")

    contenedor = ttk.LabelFrame(ventana, text="Etiquetas en un contenedor")
    contenedor.grid(column=0, row=0, padx=10, pady=10)

    ttk.Label(contenedor, text="Etiqueta1").grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(contenedor, text="Etiqueta2").grid(column=1, row=0, padx=5, pady=5)
    ttk.Label(contenedor, text="Etiqueta3").grid(column=2, row=0, padx=5, pady=5)

    ventana.mainloop()


if __name__ == "__main__":
    main()
