import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Label - método 2")

    etiqueta = ttk.Label(ventana, text="Hola Crayola!!!")
    etiqueta.grid(column=0, row=0, padx=10, pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    main()
