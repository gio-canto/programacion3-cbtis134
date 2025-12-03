import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Botón contador")
    window.geometry("300x200")

    contador = tk.IntVar(value=0)

    etiqueta = tk.Label(window, text="Has hecho clic 0 veces", font=("Arial", 12))
    etiqueta.pack(pady=10)

    def incrementar():
        contador.set(contador.get() + 1)
        etiqueta.config(text=f"Has hecho clic {contador.get()} veces")

    boton = tk.Button(window, text="Haz clic aquí", command=incrementar)
    boton.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()
