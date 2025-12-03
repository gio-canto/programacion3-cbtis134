import tkinter as tk
from tkinter import Menu, messagebox


def main():
    ventana = tk.Tk()
    ventana.title("Cajas de mensaje")

    barra_menu = Menu(ventana)
    ventana.config(menu=barra_menu)

    def mostrar_info():
        messagebox.showinfo("Información", "Este es un mensaje de información.")

    def mostrar_advertencia():
        messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")

    def mostrar_error():
        messagebox.showerror("Error", "Este es un mensaje de error.")

    mensajes_menu = Menu(barra_menu, tearoff=False)
    mensajes_menu.add_command(label="Información", command=mostrar_info)
    mensajes_menu.add_command(label="Advertencia", command=mostrar_advertencia)
    mensajes_menu.add_command(label="Error", command=mostrar_error)

    barra_menu.add_cascade(label="Mensajes", menu=mensajes_menu)

    ventana.mainloop()


if __name__ == "__main__":
    main()
