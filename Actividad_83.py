import tkinter as tk


def main():
    ventana = tk.Tk()
    ventana.title("Ventana fija (no redimensionable)")
    # No permite cambiar tamaño (ancho, alto)
    ventana.resizable(False, False)
    ventana.mainloop()


if __name__ == "__main__":
    main()
