import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Deshabilitar botón")

    def funcion_click():
        etiqueta.configure(text="Botón presionado")
        # Deshabilitar botón después del click
        boton.configure(state="disabled")

    etiqueta = ttk.Label(ventana, text="Pulsa el botón una vez")
    etiqueta.grid(column=0, row=0, padx=10, pady=10)

    boton = ttk.Button(ventana, text="Click", command=funcion_click)
    boton.grid(column=0, row=1, padx=10, pady=5)

    ventana.mainloop()


if __name__ == "__main__":
    main()
