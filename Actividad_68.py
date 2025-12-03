import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Eventos de teclado")
    window.geometry("400x200")

    etiqueta = tk.Label(window, text="Pulsa cualquier tecla…", font=("Arial", 12))
    etiqueta.pack(pady=40)

    def handle_keypress(event):
        # event.char puede estar vacío para teclas especiales
        ch = event.char if event.char else f"[{event.keysym}]"
        etiqueta.config(text=f"Tecla pulsada: {ch}")

    window.bind("<Key>", handle_keypress)

    window.mainloop()


if __name__ == "__main__":
    main()
