import tkinter as tk
from tkinter import ttk, messagebox


def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


def main():
    window = tk.Tk()
    window.title("Convertidor de temperatura")
    window.geometry("360x220")

    modo = tk.StringVar(value="C->F")

    frame = ttk.Frame(window, padding=10)
    frame.pack(expand=True, fill="both")

    ttk.Label(frame, text="Valor de temperatura:").grid(row=0, column=0, sticky="w")
    valor_var = tk.StringVar()
    entry_valor = ttk.Entry(frame, textvariable=valor_var, width=15)
    entry_valor.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame, text="Modo:").grid(row=1, column=0, sticky="w")
    opciones = ttk.Combobox(frame, textvariable=modo, values=["C->F", "F->C"], state="readonly", width=10)
    opciones.grid(row=1, column=1, padx=5, pady=5)
    opciones.current(0)

    resultado_var = tk.StringVar(value="Resultado: ")
    ttk.Label(frame, textvariable=resultado_var, font=("Arial", 12)).grid(
        row=3, column=0, columnspan=2, pady=10
    )

    def convertir():
        texto = valor_var.get().strip()
        if not texto:
            messagebox.showwarning("Aviso", "Introduce un valor numérico.")
            return
        try:
            valor = float(texto)
        except ValueError:
            messagebox.showerror("Error", "El valor debe ser un número.")
            return

        if modo.get() == "C->F":
            res = c_to_f(valor)
            resultado_var.set(f"{valor:.2f} °C = {res:.2f} °F")
        else:
            res = f_to_c(valor)
            resultado_var.set(f"{valor:.2f} °F = {res:.2f} °C")

    boton = ttk.Button(frame, text="Convertir", command=convertir)
    boton.grid(row=2, column=0, columnspan=2, pady=5)

    for i in range(2):
        frame.columnconfigure(i, weight=1)

    window.mainloop()


if __name__ == "__main__":
    main()
