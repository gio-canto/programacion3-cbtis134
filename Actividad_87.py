import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Caja de texto - Nombre")

    etiqueta = ttk.Label(ventana, text="Escribe tu nombre")
    etiqueta.grid(column=0, row=0, padx=10, pady=10)

    nombre = tk.StringVar()
    preguntar_nombre = ttk.Entry(ventana, width=20, textvariable=nombre)
    preguntar_nombre.grid(column=0, row=1, padx=10, pady=5)

    def funcion_click():
        accion.configure(text="Hola " + nombre.get())

    accion = ttk.Button(ventana, text="Haz Click Aquí!", command=funcion_click)
    accion.grid(column=1, row=1, padx=10, pady=5)

    ventana.mainloop()


if __name__ == "__main__":
    main()
