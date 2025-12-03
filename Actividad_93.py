import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


def main():
    ventana = tk.Tk()
    ventana.title("Cajas de texto (varias líneas)")

    ttk.Label(ventana, text="Escribe un texto largo:").grid(
        column=0, row=0, padx=10, pady=10, sticky=tk.W
    )

    scrol_ancho = 30
    scrol_alto = 3

    caja = scrolledtext.ScrolledText(
        ventana, width=scrol_ancho, height=scrol_alto, wrap=tk.WORD
    )
    caja.grid(column=0, row=1, padx=10, pady=5, columnspan=3)

    ventana.mainloop()


if __name__ == "__main__":
    main()
