import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Eventos con clic del ratón")
    window.geometry("400x200")

    etiqueta = tk.Label(window, text="Haz clic en cualquier parte de la ventana", font=("Arial", 11))
    etiqueta.pack(pady=40)

    def handle_click(event):
        etiqueta.config(text=f"Clic en x={event.x}, y={event.y}")

    window.bind("<Button-1>", handle_click)

    window.mainloop()


if __name__ == "__main__":
    main()
