import tkinter as tk
from tkinter import filedialog, messagebox


def main():
    window = tk.Tk()
    window.title("Editor de texto simple")
    window.geometry("600x400")

    text = tk.Text(window, wrap="word", undo=True)
    text.pack(expand=True, fill="both")

    def new_file():
        if not _maybe_discard_changes():
            return
        text.delete("1.0", tk.END)
        window.title("Editor de texto simple - Nuevo archivo")

    def open_file():
        if not _maybe_discard_changes():
            return
        filepath = filedialog.askopenfilename(
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if not filepath:
            return
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                contenido = f.read()
        except OSError as exc:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {exc}")
            return
        text.delete("1.0", tk.END)
        text.insert("1.0", contenido)
        window.title(f"Editor de texto simple - {filepath}")

    def save_file_as():
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        if not filepath:
            return
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text.get("1.0", tk.END))
        except OSError as exc:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {exc}")
            return
        window.title(f"Editor de texto simple - {filepath}")

    def _maybe_discard_changes():
        # En este ejemplo simple, siempre preguntamos sin llevar un seguimiento real
        resp = messagebox.askyesnocancel(
            "Confirmar", "¿Deseas descartar el contenido actual?"
        )
        if resp is None:
            return False  # cancelar
        return resp  # True si sí, False si no

    menu_bar = tk.Menu(window)
    file_menu = tk.Menu(menu_bar, tearoff=False)
    file_menu.add_command(label="Nuevo", command=new_file)
    file_menu.add_command(label="Abrir…", command=open_file)
    file_menu.add_command(label="Guardar como…", command=save_file_as)
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=window.quit)
    menu_bar.add_cascade(label="Archivo", menu=file_menu)

    window.config(menu=menu_bar)
    window.mainloop()


if __name__ == "__main__":
    main()
