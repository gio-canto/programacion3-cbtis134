import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Checkbuttons")

    # Casilla 1: Deshabilitada
    opcion_1 = tk.IntVar()
    casilla_1 = tk.Checkbutton(
        ventana, text="Leer", variable=opcion_1, state="disabled"
    )
    casilla_1.grid(column=0, row=0, sticky=tk.W, padx=10, pady=2)
    casilla_1.select()

    # Casilla 2: No seleccionada
    opcion_2 = tk.IntVar()
    casilla_2 = tk.Checkbutton(ventana, text="Ver películas", variable=opcion_2)
    casilla_2.grid(column=0, row=1, sticky=tk.W, padx=10, pady=2)
    casilla_2.deselect()

    # Casilla 3: Seleccionada
    opcion_3 = tk.IntVar()
    casilla_3 = tk.Checkbutton(
        ventana, text="Redes Sociales", variable=opcion_3
    )
    casilla_3.grid(column=0, row=2, sticky=tk.W, padx=10, pady=2)
    casilla_3.select()

    ventana.mainloop()


if __name__ == "__main__":
    main()
