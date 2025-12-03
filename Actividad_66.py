import tkinter as tk


def crear_frame(master, texto, relief):
    frame = tk.Frame(master, relief=relief, borderwidth=4)
    label = tk.Label(frame, text=texto, padx=10, pady=10)
    label.pack()
    return frame


def main():
    window = tk.Tk()
    window.title("Frames y relieves")
    window.geometry("500x200")

    estilos = [
        ("FLAT", tk.FLAT),
        ("RAISED", tk.RAISED),
        ("SUNKEN", tk.SUNKEN),
        ("GROOVE", tk.GROOVE),
        ("RIDGE", tk.RIDGE),
    ]

    for i, (texto, relief) in enumerate(estilos):
        frame = crear_frame(window, texto, relief)
        frame.grid(row=0, column=i, padx=5, pady=20)

    window.mainloop()


if __name__ == "__main__":
    main()
