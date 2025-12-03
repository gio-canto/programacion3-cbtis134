import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Label - método 1")

    # Agregar etiqueta directamente
    ttk.Label(ventana, text="Hola Crayola!!!").grid(column=0, row=0, padx=10, pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    main()
