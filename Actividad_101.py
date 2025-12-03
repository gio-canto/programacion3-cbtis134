import tkinter as tk
from tkinter import messagebox


def cambiar_texto():
    """Cambia el texto de la etiqueta y muestra un mensaje."""
    etiqueta.config(text="¡Hola desde Tkinter!")
    messagebox.showinfo("Información", "Texto cambiado correctamente.")


def main():
    global etiqueta

    ventana = tk.Tk()
    ventana.title("Ejercicio GUI 1 - Tkinter")
    ventana.geometry("300x200")  # ancho x alto

    etiqueta = tk.Label(ventana, text="Texto inicial", font=("Arial", 14))
    etiqueta.pack(pady=20)

    boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
    boton.pack(pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    main()
