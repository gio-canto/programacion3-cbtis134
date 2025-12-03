import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Widget Text multilínea")
    window.geometry("400x300")

    tk.Label(window, text="Escribe algo:", font=("Arial", 12)).pack()

    text = tk.Text(window, wrap="word")
    text.pack(expand=True, fill="both", padx=10, pady=10)

    def mostrar_consola():
        contenido = text.get("1.0", tk.END).strip()
        print("Contenido del Text:")
        print(contenido)

    boton = tk.Button(window, text="Imprimir en consola", command=mostrar_consola)
    boton.pack(pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()
