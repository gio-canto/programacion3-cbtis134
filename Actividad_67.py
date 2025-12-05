import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Eventos con clic del ratón")
    window.geometry("400x200")

    etiqueta1 = tk.Label(window, text="Haz clic en cualquier parte de la ventana", font=("Arial", 11))
    etiqueta1.pack(pady=20)

    # Segunda etiqueta fija al final
    etiqueta2 = tk.Label(window, text="¡⁶🤷⁷!", font=("Arial", 11))
    etiqueta2.pack(side="bottom", pady=10)

    def handle_click(event):
        etiqueta1.config(text=f"Clic en x={event.x}, y={event.y}")

    window.bind("<Button-1>", handle_click)

    window.mainloop()

if __name__ == "__main__":
    main()

