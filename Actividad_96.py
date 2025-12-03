import tkinter as tk
from tkinter import Menu


def main():
    ventana = tk.Tk()
    ventana.title("Menú con opción Salir")

    barra_menu = Menu(ventana)
    ventana.config(menu=barra_menu)

    def salir():
        ventana.destroy()

    opciones_menu = Menu(barra_menu, tearoff=False)
    opciones_menu.add_command(label="Nuevo")
    opciones_menu.add_separator()
    opciones_menu.add_command(label="Salir", command=salir)

    barra_menu.add_cascade(label="Archivo", menu=opciones_menu)

    ventana.mainloop()


if __name__ == "__main__":
    main()
