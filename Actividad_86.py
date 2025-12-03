import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Botón con evento")

    etiqueta = ttk.Label(ventana, text="Hola Crayola!!!")
    etiqueta.grid(column=0, row=0, padx=10, pady=10)

    def funcion_click():
        accion.configure(text="** Haz hecho Click! **")
        etiqueta.configure(foreground="red")

    accion = ttk.Button(ventana, text="Haz Click Aquí!", command=funcion_click)
    accion.grid(column=1, row=0, padx=10, pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    main()
