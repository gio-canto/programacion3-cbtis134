import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Radiobuttons - Colores")

    COLOR1 = "blue"
    COLOR2 = "gold"
    COLOR3 = "red"

    opcion = tk.IntVar(value=1)

    def funcion_radio():
        selector = opcion.get()
        if selector == 1:
            ventana.configure(background=COLOR1)
        elif selector == 2:
            ventana.configure(background=COLOR2)
        elif selector == 3:
            ventana.configure(background=COLOR3)

    ttk.Label(ventana, text="Elige un color:").grid(
        column=0, row=0, padx=10, pady=10, sticky=tk.W
    )

    radio1 = tk.Radiobutton(
        ventana, text=COLOR1.title(), variable=opcion, value=1, command=funcion_radio
    )
    radio1.grid(column=0, row=1, sticky=tk.W, padx=10)

    radio2 = tk.Radiobutton(
        ventana, text=COLOR2.title(), variable=opcion, value=2, command=funcion_radio
    )
    radio2.grid(column=0, row=2, sticky=tk.W, padx=10)

    radio3 = tk.Radiobutton(
        ventana, text=COLOR3.title(), variable=opcion, value=3, command=funcion_radio
    )
    radio3.grid(column=0, row=3, sticky=tk.W, padx=10)

    ventana.configure(background=COLOR1)

    ventana.mainloop()


if __name__ == "__main__":
    main()
