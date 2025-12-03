import tkinter as tk
from tkinter import PhotoImage


def main():
    win = tk.Tk()
    win.title("Información del estudiante")
    win.geometry("500x250+250+250")

    L1 = tk.Label(win, text="Información del estudiante", font=("Helvetica", 20, "bold"))
    L2 = tk.Label(win, text="ID del estudiante:", font=("Helvetica", 14))
    L3 = tk.Label(win, text="Nombre:", font=("Helvetica", 14))
    L4 = tk.Label(win, text="Importante:", font=("Helvetica", 14))

    L1.grid(row=0, column=1, columnspan=2, pady=5)
    L2.grid(row=1, column=0, sticky="e", pady=5)
    L3.grid(row=2, column=0, sticky="e", pady=5)
    L4.grid(row=3, column=0, sticky="e", pady=5)

    # ---- cargar imagen y reducirla ----
    try:
        photo = PhotoImage(file="f1.png")

        # REDUCCIÓN DE TAMAÑO
        photo = photo.subsample(3, 3)  # prueba 3x más pequeño

        LP = tk.Label(win, image=photo)
        LP.image = photo  # evitar que se borre
        LP.grid(row=0, column=2, rowspan=4, padx=10, pady=5)
    except Exception as e:
        LP = tk.Label(win, text=f"Sin imagen\n({e})")
        LP.grid(row=0, column=2, rowspan=4, padx=10, pady=5)

    e1 = tk.Entry(win, width=20, font=("Helvetica", 14))
    e2 = tk.Entry(win, width=20, font=("Helvetica", 14))
    e3 = tk.Entry(win, width=20, font=("Helvetica", 14))

    e1.grid(row=1, column=1, pady=5)
    e2.grid(row=2, column=1, pady=5)
    e3.grid(row=3, column=1, pady=5)

    win.mainloop()


if __name__ == "__main__":
    main()
