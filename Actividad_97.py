import tkinter as tk
from tkinter import ttk


def main():
    ventana = tk.Tk()
    ventana.title("Pestañas - Notebook")

    notebook = ttk.Notebook(ventana)
    notebook.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")

    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)

    notebook.add(frame1, text="Pestaña 1")
    notebook.add(frame2, text="Pestaña 2")

    ttk.Label(frame1, text="Contenido de la pestaña 1").grid(
        column=0, row=0, padx=10, pady=10
    )
    ttk.Label(frame2, text="Contenido de la pestaña 2").grid(
        column=0, row=0, padx=10, pady=10
    )

    ventana.mainloop()


if __name__ == "__main__":
    main()
