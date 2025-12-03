import tkinter as tk
from tkinter import messagebox


def main():
    window = tk.Tk()
    window.title("Saludo con Entry")
    window.geometry("350x200")

    tk.Label(window, text="Escribe tu nombre:").pack(pady=5)
    nombre_var = tk.StringVar()
    entry = tk.Entry(window, textvariable=nombre_var)
    entry.pack(pady=5)

    etiqueta = tk.Label(window, text="", font=("Arial", 12))
    etiqueta.pack(pady=10)

    def saludar():
        nombre = nombre_var.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Escribe un nombre primero.")
            return
        mensaje = f"Hola, {nombre}!"
        etiqueta.config(text=mensaje)

    boton = tk.Button(window, text="Saludar", command=saludar)
    boton.pack(pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()
