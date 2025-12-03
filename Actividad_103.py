import tkinter as tk
from tkinter import messagebox


def main():
    ventana = tk.Tk()
    ventana.title("Lista Interactiva")
    ventana.geometry("300x300")

    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

    lista = tk.Listbox(ventana)
    lista.pack(expand=True, fill="both", pady=10)

    def agregar():
        item = entrada.get().strip()
        if item:
            lista.insert(tk.END, item)
            entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes agregar un texto vacío.")

    def eliminar():
        seleccion = lista.curselection()
        if seleccion:
            lista.delete(seleccion[0])
        else:
            messagebox.showwarning("Advertencia", "Selecciona un elemento para eliminar.")

    tk.Button(ventana, text="Agregar", command=agregar).pack()
    tk.Button(ventana, text="Eliminar", command=eliminar).pack()

    ventana.mainloop()


if __name__ == "__main__":
    main()
