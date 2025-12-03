import tkinter as tk
from tkinter import Menu


def main():
    ventana = tk.Tk()
    ventana.title("Barra de menús")

    barra_menu = Menu(ventana)
    ventana.config(menu=barra_menu)

    opciones_menu = Menu(barra_menu, tearoff=False)
    opciones_menu.add_command(label="Nuevo")
    opciones_menu.add_command(label="Salir")

    barra_menu.add_cascade(label="Archivo", menu=opciones_menu)

    ventana.mainloop()


if __name__ == "__main__":
    main()
